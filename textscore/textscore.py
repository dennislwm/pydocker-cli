#--------------------------
# Create a command line app
import click
#--------------------------
# Score readability of text
import textstat
#-------------------------
# Convert markdown to text
import mdtotext
#-----------------
# Standard library
import glob
import math
import os

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                    M A I N   C L A S S                                   |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
class Textscore(object):

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                                   C O N S T R U C T O R                                  |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""
  def __init__(self, out, textfile):
    #----------------------------
    # initialize class _CONSTANTS
    self._init_meta()

    #----------------
    # Class variables
    self.automated_readability_index = 0.0
    self.str_automated_readability_index = ''
    self.coleman_liau_index = 0.0
    self.str_coleman_liau_index = ''
    self.dale_chall_readability_score = 0.0
    self.str_dale_chall_readability_score = ''
    self.difficult_words = 0
    self.flesch_kincaid_grade = 0.0
    self.str_flesch_kincaid_grade = ''
    self.flesch_reading_ease = 0.0
    self.str_flesch_reading_ease = ''
    self.gunning_fog = 0.0
    self.str_gunning_fog = ''
    self.linsear_write_formula = 0.0
    self.str_linsear_write_formula = ''
    self.smog_index = 0.0
    self.str_smog_index = ''
    self.text_standard = ""

    #-------------------------
    # Initialize click objects
    self.out = out
    self.textfile = textfile

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                        E X T E R N A L   C L A S S   M E T H O D S                       |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""
  def pipe(self):
    docs = glob.glob(self.textfile, recursive=True)
    for doc in docs:
      strExt = os.path.splitext(doc)[1]
      if strExt == '.md' or strExt == '.txt':
        #--------------------------------------------- 
        # Read file and process markdown, docx to text
        f = open(doc, 'r')
        strText = f.read()
        if strExt == '.md':
          strText = mdtotext.unmark(strText)

        #----------------------------
        # Score text and print result
        self.score(strText)
        if self.out == 'text':
          self.print_text(doc)

        #----------------------------
        # Close file and move to next
        f.close()

  def score(self, strText):
    self.automated_readability_index = textstat.automated_readability_index(strText)
    self.str_automated_readability_index = self.grade(self.automated_readability_index)

    self.coleman_liau_index = textstat.coleman_liau_index(strText)
    self.str_coleman_liau_index = self.grade(self.coleman_liau_index)

    self.dale_chall_readability_score = textstat.dale_chall_readability_score(strText)
    if self.dale_chall_readability_score >= 9.0:
      self.str_dale_chall_readability_score = ' | ' + '13th to 15th grade (college)'
    elif self.dale_chall_readability_score >= 8.0:
      self.str_dale_chall_readability_score = ' | ' + '11th to 12th grade'
    elif self.dale_chall_readability_score >= 7.0:
      self.str_dale_chall_readability_score = ' | ' + '9th to 10th grade'
    elif self.dale_chall_readability_score >= 6.0:
      self.str_dale_chall_readability_score = ' | ' + '7th to 8th grade'
    elif self.dale_chall_readability_score >= 5.0:
      self.str_dale_chall_readability_score = ' | ' + '5th to 6th grade'
    else:
      self.str_dale_chall_readability_score = ' | ' + '4th grade or lower'

    self.difficult_words = textstat.difficult_words(strText)

    self.flesch_kincaid_grade = textstat.flesch_kincaid_grade(strText)
    self.str_flesch_kincaid_grade = self.grade(self.flesch_kincaid_grade)

    self.flesch_reading_ease = textstat.flesch_reading_ease(strText)
    if self.flesch_reading_ease >= 90:
      self.str_flesch_reading_ease = ' | ' + 'Very Easy'
    elif self.flesch_reading_ease >= 80:
      self.str_flesch_reading_ease = ' | ' + 'Easy'
    elif self.flesch_reading_ease >= 70:
      self.str_flesch_reading_ease = ' | ' + 'Fairly Easy'
    elif self.flesch_reading_ease >= 60:
      self.str_flesch_reading_ease = ' | ' + 'Standard'
    elif self.flesch_reading_ease >= 50:
      self.str_flesch_reading_ease = ' | ' + 'Fairly Difficult'
    elif self.flesch_reading_ease >= 30:
      self.str_flesch_reading_ease = ' | ' + 'Difficult'
    else:
      self.str_flesch_reading_ease = ' | ' + 'Very Confusing'

    self.gunning_fog = textstat.gunning_fog(strText)
    self.str_gunning_fog = self.grade(self.gunning_fog)
    
    self.linsear_write_formula = textstat.linsear_write_formula(strText)
    self.str_linsear_write_formula = self.grade(self.linsear_write_formula)

    self.smog_index = textstat.smog_index(strText)
    self.str_smog_index = self.grade(self.smog_index)

    self.text_standard = textstat.text_standard(strText)

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                        I N T E R N A L   C L A S S   M E T H O D S                       |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""

  def grade(self, score):
    strRet = ''
    if score > 0:
      strRet = ' | ' + str( math.floor(score) ) + 'th grade'
    return strRet

  def print_text(self, strFile):
    print('\r')
    print('Document:                     ' + strFile)
    print('Flesch Reading Ease:          ' + str(self.flesch_reading_ease) + self.str_flesch_reading_ease)
    print('Smog Index:                   ' + str(self.smog_index) + self.str_smog_index)
    print('Flesch Kincaid Grade:         ' + str(self.flesch_kincaid_grade) + self.str_flesch_kincaid_grade)
    print('Coleman Liau Index:           ' + str(self.coleman_liau_index) + self.str_coleman_liau_index)
    print('Automated Readability Index:  ' + str(self.automated_readability_index) + self.str_automated_readability_index)
    print('Dale Chall Readability Score: ' + str(self.dale_chall_readability_score) + self.str_dale_chall_readability_score)
    print('Difficult Words:              ' + str(self.difficult_words))
    print('Linsear Write Formula:        ' + str(self.linsear_write_formula) + self.str_linsear_write_formula)
    print('Gunning Fog:                  ' + str(self.gunning_fog) + self.str_gunning_fog)
    print('Text Standard (Consensus):    ' + str(self.text_standard))

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                                C L A S S   M E T A D A T A                               |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""
  def _init_meta(self):
      """
      | _strMETACLASS, _strMETAVERSION, _strMETAFILE used to save() and load() members
      """
      self._strMETACLASS = str(self.__class__).split('.')[1][:-2]
      self._strMETAVERSION = "0.1"
      """
      | Filename "_Class_Version_"
      """
      self._strMETAFILE = "_" + self._strMETACLASS + "_" + self._strMETAVERSION + "_"

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                  M A I N   C O M M A N D                                 |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
@click.command( context_settings=dict(help_option_names=['-h', '--help']) )
#---------------
# Choice options
@click.option('--out', '-o', default='text', 
  type=click.Choice([
    'csv',
    'json',
    'markdown',
    'text'
  ]),
  help='Output type, default=text')
@click.argument('textfile')
#--------------
# Main function
def clickMain(out, textfile):
  """
  This script scores the readability of a TEXTFILE
  
  TEXTFILE may include wildcards, e.g. *.txt
  """
  objTextscore = Textscore(out, textfile)
  objTextscore.pipe()

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                M A I N   P R O C E D U R E                               |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
if __name__ == "__main__":
  clickMain()
