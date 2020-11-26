#------------
# Web request
import requests
#------------
# Html parser
from bs4 import BeautifulSoup
import lxml
#-----------------
# Standard library
import json
import re

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                    M A I N   C L A S S                                   |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
class Pybiblia():

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                                   C O N S T R U C T O R                                  |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""
  def __init__(self, strApiKey):
    #----------------------------
    # initialize class _CONSTANTS
    assert(strApiKey)
    self._init_meta()

    self.BIBLIA_API_KEY = strApiKey
    self.strUrlBase = 'https://api.biblia.com/v1/bible'
    self.strUrlToken = '?key=' + self.BIBLIA_API_KEY

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                                C L A S S   R E Q U E S T S                               |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""

  def content(self, bible, passage):
    """ Returns the content of a bible """
    assert(bible)
    assert(passage)
    if bible == 'rsvce':
      return self.rsvce(passage)
    else:
      strOutput = '.txt'
      strPassage = '&passage=' + passage
      res = requests.get(self.strUrlBase + '/content/' + bible + strOutput + self.strUrlToken + strPassage)
      if not res:
        return self.json_error()
      return res.text

  def rsvce(self, passage):
    """ Returns the content of the Revised Standard Edition Catholic Edition (RSVCE) """
    assert(passage)
    strUrlBase = 'https://biblia.com/bible/rsvce'
    objRes = requests.get(strUrlBase + '/' + passage)
    objSoup = BeautifulSoup(objRes.content, 'lxml') 
    #----------------------------
    # 1/3 Scrape all the div tags
    refs = []
    for div in objSoup.find_all('div', attrs={'class': 'resourcetext'}):
      refs.append(div)
      #----------------------------
      # Uncomment to debug raw html
      #print(len(refs))
      #print(str(div) + '\r')
      #print(str(div.text))
    #-----------------------------------------
    # 2/3 From the div tag use Regex find text
    objRegex = re.sub(r"(^|\W)\d+","",refs[0].text)
    #-----------------------------
    # 3/3 Split string to get text 
    strRegex = objRegex.lstrip()
    return strRegex

  def search(self, bible, query):
    """ Searches the text of a bible """
    strOutput = '.txt'
    strQuery = '&query=' + query
    res = requests.get(self.strUrlBase + '/search/' + bible + strOutput + self.strUrlToken + strQuery)
    if not res:
      return self.json_error()
    return res.json()

  def toc(self, bible):
    """ Returns the table of contents of a bible """
    assert(bible)
    res = requests.get(self.strUrlBase + '/contents/' + bible + self.strUrlToken)
    if not res:
      return self.json_error()
    return res.json()

  def votd(self, bible):
    """ Returns a carefully chosen verse each day """
    assert(bible)
    strUrlBase = 'https://biblia.com/api/plugins/verseoftheday'
    objRes = requests.get(strUrlBase + '/' + bible)
    objSoup = BeautifulSoup(objRes.content, 'lxml') 
    #-------------------------------
    # 1/3 Scrape all the anchor tags
    refs = []
    for a in objSoup.find_all('a', href=True):
      refs.append(a)
      #----------------------------
      # Uncomment to debug raw html
      #print(len(refs))
      #print(str(a) + '\r')
      #print(str(a.text))
    #-----------------------------------------------
    # 2/3 From the anchor tag use Regex find passage
    objRegex = re.search('ref.ly/[A-Z,a-z]+[1-9]+.[1-9]+;', str(refs[2]))
    strRegex = objRegex.group(0)
    #--------------------------------
    # 3/3 Split string to get passage
    passage = strRegex.split('/')[1]
    strRet = passage.split(';')[0]
    return strRet

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                                 C L A S S   M E T H O D S                                |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""
  def json_error():
    jsnRet = json.dumps({})
    jsnRet['error_code'] = 1
    jsnRet['error_msg'] = 'Failed request'
    return jsnRet

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
