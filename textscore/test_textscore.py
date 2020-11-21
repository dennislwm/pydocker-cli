from textscore import clickMain
from click.testing import CliRunner

strText = ''

def test_print_text():
  runner = CliRunner()
  result = runner.invoke(clickMain, ['TEXT'])
  assert result.exit_code == 0
  assert "Text Standard" in result.output 

def test_print_markdown():
  runner = CliRunner()
  result = runner.invoke(clickMain, ['--out', 'markdown', 'TEXT'])
  assert result.exit_code == 0
  assert "Text Standard" in result.output 


"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                M A I N   P R O C E D U R E                               |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
def main():
  test_print_markdown()
  test_print_text()

if __name__ == "__main__":
  main()
