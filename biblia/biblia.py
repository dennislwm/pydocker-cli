#--------------------------
# Create a command line app
import click
#-----------
# Biblia API
from pybiblia import Pybiblia
#-----------------
# Standard library
import json
import os

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                    M A I N   C L A S S                                   |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
class Biblia(object):

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                                   C O N S T R U C T O R                                  |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""
  def __init__(self, out):
    #----------------------------
    # initialize class _CONSTANTS
    self._init_meta()

    #----------------
    # Class variables
    self.load_config()

    #-------------------------
    # Initialize click objects
    self.out = out
    self.objBiblia = Pybiblia(self.API_KEY)

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                        E X T E R N A L   C L A S S   M E T H O D S                       |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""
  def content(self, bible, passage):
    result = self.objBiblia.content(bible, passage)
    print( result )

  def search(self, bible, query):
    result = self.objBiblia.search(bible, query)
    self.print_result( result )

  def toc(self, bible):
    result = self.objBiblia.toc(bible)
    self.print_result( result )

  def votd(self, bible):
    passage = self.objBiblia.votd(bible)
    result = self.objBiblia.content(bible, passage)
    print( passage )
    print( result )

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                        I N T E R N A L   C L A S S   M E T H O D S                       |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""
  def load_config(self):
    self.API_KEY = ""

    #---------------------------
    # Load environment variables
    if 'BIBLIA_API_KEY' in os.environ:
      self.API_KEY = os.environ['BIBLIA_API_KEY']

    #--------------------------------------
    # A JSON file supercedes os environment
    if os.path.exists("config.json"):
        with open("config.json", 'r') as f:
            config = json.load(f)
            if 'BIBLIA_API_KEY' in config:
              self.API_KEY = config['BIBLIA_API_KEY']

  def print_result(self, result):
    if self.out == 'text':
      strText = json.dumps(result, indent=4, separators=(',', ': '))
      strText = strText.replace('[', '')
      strText = strText.replace(']', '')
      strText = strText.replace('{', '')
      strText = strText.replace('}', '')
      strText = strText.replace(',', '')
      strText = strText.replace('\"', '')
      strText = strText.replace('    \n', '')
      strText = strText.replace('    ', '')
      print(strText)

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
@click.group( context_settings=dict(help_option_names=['-h', '--help']) )
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
@click.pass_context
#--------------
# Main function
def clickMain(ctx, out):
  """
  This script prints bible data
  """
  ctx.obj = Biblia(out)

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                               C O N T E N T   C O M M A N D                              |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
@clickMain.command()
#---------------
# Choice options
@click.option('--bible', '-b', default='asv', 
  type=click.Choice([
    'asv',
    'esv',
    'kjv',
    'leb',
    'rsvce',
    'ylt'
  ]),
  help='Bible code, default=asv')
@click.argument('passage', required=True)
@click.pass_obj
#---------
# Function
def content(objBiblia, bible, passage):
  """ Returns the content of a bible """
  objBiblia.content(bible, passage)

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                S E A R C H   C O M M A N D                               |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
@clickMain.command()
#---------------
# Choice options
@click.option('--bible', '-b', default='asv', 
  type=click.Choice([
    'asv',
    'esv',
    'kjv',
    'leb',
    'ylt'
  ]),
  help='Bible code, default=asv')
@click.argument('query', required=True)
@click.pass_obj
#---------
# Function
def search(objBiblia, bible, query):
  """ Searches the text of a bible """
  objBiblia.search(bible, query)

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                   T O C   C O M M A N D                                  |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
@clickMain.command()
#---------------
# Choice options
@click.option('--bible', '-b', default='asv', 
  type=click.Choice([
    'asv',
    'esv',
    'kjv',
    'leb',
    'ylt'
  ]),
  help='Bible code, default=asv')
@click.pass_obj
#---------
# Function 
def toc(objBiblia, bible):
  """ Returns the table of contents of a bible """
  objBiblia.toc(bible)

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                  V O T D   C O M M A N D                                 |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
@clickMain.command()
#---------------
# Choice options
@click.option('--bible', '-b', default='asv', 
  type=click.Choice([
    'asv',
    'esv',
    'kjv',
    'leb',
    'rsvce',
    'ylt'
  ]),
  help='Bible code, default=asv')
@click.pass_obj
#---------
# Function 
def votd(objBiblia, bible):
  """ Returns a carefully chosen verse each day """
  objBiblia.votd(bible)

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                M A I N   P R O C E D U R E                               |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
if __name__ == "__main__":
  clickMain()
