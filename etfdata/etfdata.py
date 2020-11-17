import click
import finnhub
from finnhub_api import FinnhubApi
import json
import os
import pandas as pd

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                    M A I N   C L A S S                                   |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
class Etfdata(object):

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                                   C O N S T R U C T O R                                  |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""
  def __init__(self, out):
    #----------------------------
    # initialize class _CONSTANTS
    self._init_meta()

    self.FINNHUB_API_KEY = ""
    #---------------------------
    # Load environment variables
    if 'FINNHUB_API_KEY' in os.environ:
      self.FINNHUB_API_KEY = os.environ['FINNHUB_API_KEY']

    #--------------------------------------
    # A JSON file supercedes os environment
    if os.path.exists("config.json"):
        with open("config.json", 'r') as f:
            config = json.load(f)
            if 'FINNHUB_API_KEY' in config:
              self.FINNHUB_API_KEY = config['FINNHUB_API_KEY']

    #-------------------------
    # Initialize class objects
    self.out = out
    self.objFinn = finnhub.Client(api_key=self.FINNHUB_API_KEY)
    self.apiFinn = FinnhubApi(self.FINNHUB_API_KEY)

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                                C L A S S   R E Q U E S T S                               |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""
  def cal_economic(self):
    result = self.apiFinn.cal_economic()
    self.print_result( result )

  def etf_country(self, stocks):
    for stock in stocks:
      result = self.objFinn.etfs_country_exp(symbol=stock)
      self.print_result( result )

  def etf_holdings(self, stocks):
    for stock in stocks:
      result = self.objFinn.etfs_holdings(symbol=stock)
      self.print_result( result )

  def etf_profile(self, stocks):
    for stock in stocks:
      result = self.objFinn.etfs_profile(symbol=stock)
      self.print_result( result )

  def etf_sector(self, stocks):
    for stock in stocks:
      result = self.objFinn.etfs_ind_exp(symbol=stock)
      self.print_result( result )

  def list_all(self, exchange):
    result = self.objFinn.stock_symbols(exchange)
    self.print_result( result )

  def news_forex(self):
    result = self.objFinn.general_news('forex')
    self.print_result( result )

  def news_general(self):
    result = self.objFinn.general_news('general')
    self.print_result( result )

  def stock_eps(self, stocks):
    for stock in stocks:
      result = self.objFinn.company_earnings(stock)
      self.print_result( result )

  def stock_metric(self, stocks):
    for stock in stocks:
      result = self.objFinn.company_basic_financials(stock, 'all')
      self.print_result( result )

  def stock_peers(self, stocks):
    for stock in stocks:
      result = self.objFinn.company_peers(stock)
      self.print_result( result )

  def stock_price(self, stocks):
    for stock in stocks:
      result = self.objFinn.quote(stock)
      self.print_result( result )

  def stock_price_target(self, stocks):
    for stock in stocks:
      result = self.objFinn.price_target(stock)
      self.print_result( result )

  def stock_profile(self, stocks):
    for stock in stocks:
      result = self.objFinn.company_profile2(symbol=stock)
      self.print_result( result )

  def stock_recommendation(self, stocks):
    for stock in stocks:
      result = self.objFinn.recommendation_trends(stock)
      self.print_result( result )

  def stock_sentiment(self, stocks):
    for stock in stocks:
      result = self.objFinn.news_sentiment(stock)
      self.print_result( result )

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                                 C L A S S   M E T H O D S                                |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""

  def print_result(self, result):
    if self.out == 'text':
      print( json.dumps(result, indent=4, separators=(',', ': ')) )

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
  """ This script prints etf and stock data """
  ctx.obj = Etfdata(out)

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                   C O M M A N D   C A L                                  |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
@clickMain.command()
#---------------
# Choice options
@click.option('--category', '-c', default='economic', 
  type=click.Choice([
    'economic',
    'ipo'
  ]),
  help='Calendar, default=economic')
@click.pass_obj
#-----------------
# Function econ()
def cal(etfdata, category):
  """ Economic calendar """
  click.echo("Calendar " + category)

  if category == 'economic':
    etfdata.cal_economic()

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                   C O M M A N D   E T F                                  |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
@clickMain.command()
#---------------
# Choice options
@click.option('--fundamental', '-f', default='holdings', 
  type=click.Choice([
    'country',
    'holdings',
    'profile',
    'sector'
  ]),
  help='ETF fundamentals, default=holdings')
@click.argument('symbols', required=True, nargs=-1)
@click.pass_obj
#---------------
# Function etf()
def etf(etfdata, fundamental, symbols):
  """ ETF fundamentals """
  click.echo("ETF fundamentals")

  if fundamental=='country':
    etfdata.etf_country(symbols)
  if fundamental=='holdings':
    etfdata.etf_holdings(symbols)
  if fundamental=='profile':
    etfdata.etf_profile(symbols)
  if fundamental=='sector':
    etfdata.etf_sector(symbols)

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                  C O M M A N D   N E W S                                 |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
@clickMain.command()
#---------------
# Choice options
@click.option('--category', '-c', default='general', 
  type=click.Choice([
    'business',
    'crypto',
    'finance',
    'forex',
    'general',
    'merger',
    'technology'
  ]),
  help='News category, default=general')
@click.pass_obj
#----------------
# Function news()
def news(etfdata, category):
  """ Latest market news """
  click.echo("Latest market news " + category)

  if category == 'forex':
    etfdata.news_forex()
  if category == 'general':
    etfdata.news_general()

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                  C O M M A N D   L I S T                                 |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
@clickMain.command()
#---------------
# Choice options
@click.option('--exchange', '-x', default='US', 
  type=click.Choice([
    'AX',
    'HK',
    'KL',
    'KQ',
    'KS',
    'L',
    'NZ',
    'SI',
    'SS',
    'SZ',
    'T',
    'TO',
    "TW",
    'US'
  ]),
  help='Exchange code, default=US')
#---------------
# Choice options
@click.option('--type', '-t', default='all', 
  type=click.Choice([
    'all',
    'etf'
  ]),
  help='Type, default=all')
@click.pass_obj
#----------------
# Function list()
def list(etfdata, exchange, type):
  """ List of symbols """
  click.echo("List of symbols in " + exchange)

  if type == 'all':
    etfdata.list_all(exchange)

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                 C O M M A N D   S T O C K                                |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
@clickMain.command()
#---------------
# Choice options
@click.option('--fundamental', '-f', default='price',
  type=click.Choice([
    'eps',
    'metric', 
    'peers', 
    'price',
    'price-target', 
    'profile', 
    'recommendation', 
    'sentiment'
  ]), 
  help='Stock fundamentals, default=price')
@click.argument('symbols', required=True, nargs=-1)
@click.pass_obj
#-----------------
# Function stock()
def stock(etfdata, fundamental, symbols):
  """ 
    Stock fundamentals of SYMBOLS 

    where SYMBOLS is one or more US-listed symbols separated by space
  """
  click.echo(fundamental)

  if fundamental=='eps':
    etfdata.stock_eps(symbols)
  if fundamental=='metric':
    etfdata.stock_metric(symbols)
  if fundamental=='peers':
    etfdata.stock_peers(symbols)
  if fundamental=='price':
    etfdata.stock_price(symbols)
  if fundamental=='price-target':
    etfdata.stock_price_target(symbols)
  if fundamental=='profile':
    etfdata.stock_profile(symbols)
  if fundamental=='recommendation':
    etfdata.stock_recommendation(symbols)
  if fundamental=='sentiment':
    etfdata.stock_sentiment(symbols)

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                M A I N   P R O C E D U R E                               |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
if __name__ == "__main__":
  clickMain()
