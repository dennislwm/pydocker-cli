import json
import requests

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                    M A I N   C L A S S                                   |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
class FinnhubApi():

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                                   C O N S T R U C T O R                                  |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""
  def __init__(self, strApiKey):
    #----------------------------
    # initialize class _CONSTANTS
    self._init_meta()

    self.FINNHUB_API_KEY = strApiKey
    self.strUrlBase = 'https://finnhub.io/api/v1'
    self.strUrlToken = '?token=' + self.FINNHUB_API_KEY

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                                C L A S S   R E Q U E S T S                               |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""
  def cal_economic(self):
    ''' Note ID is taken from inkdrop.app '''
    res = requests.get(self.strUrlBase + '/calendar/economic' + self.strUrlToken)
    if not res:
      return self.json_error()

    return res.json()

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
