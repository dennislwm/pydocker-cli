import click

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                    M A I N   C L A S S                                   |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
class Etfdata(object):

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                                   C O N S T R U C T O R                                  |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""
  def __init__(self):
    #----------------------------
    # initialize class _CONSTANTS
    self._init_meta()
                
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
def clickMain(ctx):
  """ This script prints etf and stock data """
  ctx.obj = Etfdata()

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                  C O M M A N D   E C O N                                 |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
@clickMain.command()
@click.pass_obj
#-----------------
# Function econ()
def econ(etfdata):
  """ Economic calendar """
  click.echo("Economic calendar")

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                   C O M M A N D   E T F                                  |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
@clickMain.command()
#---------------
# Choice options
@click.option('--fundamental', '-f', default='general', 
  type=click.Choice([
    'constituents',
    'country',
    'sector'
  ]),
  help='ETF fundamentals, default=constituents')
@click.pass_obj
#---------------
# Function etf()
def etf(etfdata, fundamental):
  """ ETF fundamentals """
  click.echo("ETF fundamentals")

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                  C O M M A N D   N E W S                                 |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
@clickMain.command()
#---------------
# Choice options
@click.option('--category', '-c', default='general', 
  type=click.Choice([
    'crypto',
    'forex',
    'general',
    'merger'
  ]),
  help='News category, default=general')
@click.pass_obj
#----------------
# Function news()
def news(etfdata, category):
  """ Latest market news """
  click.echo("Latest market news " + category)

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
@click.pass_obj
#----------------
# Function list()
def list(etfdata, exchange):
  """ List of symbols """
  click.echo("List of symbols in " + exchange)

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                 C O M M A N D   S T O C K                                |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
@clickMain.command()
#---------------
# Choice options
@click.option('--fundamental', '-f', default='quote',
  type=click.Choice([
    'eps-surprises',
    'metric', 
    'peers', 
    'price-target', 
    'profile', 
    'quote',
    'recommendation', 
    'sentiment'
  ]), 
  help='Stock fundamentals, default=quote')
@click.argument('symbols', required=True, nargs=-1)
@click.pass_obj
#-----------------
# Function stock()
def stock(etfdata, fundamental, symbols):
  """ 
    Stock fundamentals of SYMBOLS 

    SYMBOLS is one or more US-listed symbols separated by space
  """
  click.echo(fundamental)
  for sym in symbols:
    click.echo(sym)

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                M A I N   P R O C E D U R E                               |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
if __name__ == "__main__":
  clickMain()
