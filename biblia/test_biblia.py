from biblia import clickMain
from click.testing import CliRunner

strBible = 'asv'
strPassage = 'Lk21.28'
strQuery = 'gnashing'

def test_content():
  runner = CliRunner()
  result = runner.invoke(clickMain, ['content', strPassage])
  assert result.exit_code == 0
  assert "But when these things begin to come to pass" in result.output 
  result = runner.invoke(clickMain, ['content', '-b', 'rsvce', strPassage])
  assert result.exit_code == 0
  assert "Now when these things begin to take place" in result.output 

def test_search():
  runner = CliRunner()
  result = runner.invoke(clickMain, ['search', strQuery])
  assert result.exit_code == 0
  assert "Acts 7:54" in result.output 

def test_toc():
  runner = CliRunner()
  result = runner.invoke(clickMain, ['toc'])
  assert result.exit_code == 0
  assert "Revelation" in result.output 

def test_votd():
  runner = CliRunner()
  result = runner.invoke(clickMain, ['votd'])
  assert result.exit_code == 0
  assert "." in result.output 

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                M A I N   P R O C E D U R E                               |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
def main():
  test_content()
  test_search()
  test_toc()
  test_votd()

if __name__ == "__main__":
  main()
