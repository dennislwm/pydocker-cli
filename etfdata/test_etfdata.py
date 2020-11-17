from etfdata import clickMain
from click.testing import CliRunner

strSymbolEtf = 'ARKK'
strSymbolStock = 'AAPL'

def test_cal_economic():
  runner = CliRunner()
  result = runner.invoke(clickMain, ['cal'])
  assert result.exit_code == 0
  assert "event" in result.output 

def test_etf_country():
  runner = CliRunner()
  result = runner.invoke(clickMain, ['etf', '-f', 'country', strSymbolEtf])
  assert result.exit_code == 0
  assert "exposure" in result.output 

def test_etf_sector():
  runner = CliRunner()
  result = runner.invoke(clickMain, ['etf', '-f', 'sector', strSymbolEtf])
  assert result.exit_code == 0
  assert "percent" in result.output 

def test_list_all():
  runner = CliRunner()
  result = runner.invoke(clickMain, ['list'])
  assert result.exit_code == 0
  assert "displaySymbol" in result.output 

def test_list_etf():
  pass

def test_news_business():
  pass

def test_news_crypto():
  pass

def test_news_finance():
  pass

def test_news_merger():
  pass

def test_news_technology():
  pass

def test_news_forex():
  runner = CliRunner()
  result = runner.invoke(clickMain, ['news', '-c', 'forex'])
  assert result.exit_code == 0
  assert "forex" in result.output 

def test_news_general():
  runner = CliRunner()
  result = runner.invoke(clickMain, ['news'])
  assert result.exit_code == 0
  assert "summary" in result.output 

def test_stock_eps():
  runner = CliRunner()
  result = runner.invoke(clickMain, ['stock', '-f', 'eps', strSymbolStock])
  assert result.exit_code == 0
  assert "actual" in result.output 

def test_stock_metric():
  runner = CliRunner()
  result = runner.invoke(clickMain, ['stock', '-f', 'metric', strSymbolStock])
  assert result.exit_code == 0
  assert "totalRatio" in result.output 

def test_stock_peers():
  runner = CliRunner()
  result = runner.invoke(clickMain, ['stock', '-f', 'peers', strSymbolStock])
  assert result.exit_code == 0
  assert strSymbolStock in result.output 

def test_stock_price():
  runner = CliRunner()
  result = runner.invoke(clickMain, ['stock', strSymbolStock])
  assert result.exit_code == 0
  assert "pc" in result.output 

def test_stock_price_target():
  runner = CliRunner()
  result = runner.invoke(clickMain, ['stock', '-f', 'price-target', strSymbolStock])
  assert result.exit_code == 0
  assert "targetMean" in result.output 

def test_stock_profile():
  runner = CliRunner()
  result = runner.invoke(clickMain, ['stock', '-f', 'profile', strSymbolStock])
  assert result.exit_code == 0
  assert "marketCapitalization" in result.output 

def test_stock_recommendation():
  runner = CliRunner()
  result = runner.invoke(clickMain, ['stock', '-f', 'recommendation', strSymbolStock])
  assert result.exit_code == 0
  assert "strongBuy" in result.output 

def test_stock_sentiment():
  runner = CliRunner()
  result = runner.invoke(clickMain, ['stock', '-f', 'sentiment', strSymbolStock])
  assert result.exit_code == 0
  assert "bullishPercent" in result.output 

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                M A I N   P R O C E D U R E                               |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
def main():
  test_cal_economic()
  test_etf_country()
  test_etf_sector()
  test_list_all()
  test_list_etf()
  test_news_business()
  test_news_crypto()
  test_news_finance()
  test_news_forex()
  test_news_general()
  test_news_merger()
  test_news_technology()
  test_stock_eps()
  test_stock_metric()
  test_stock_peers()
  test_stock_price()
  test_stock_price_target()
  test_stock_profile()
  test_stock_recommendation()
  test_stock_sentiment()

if __name__ == "__main__":
  main()
