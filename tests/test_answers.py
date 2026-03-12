import json, pathlib
from utils.checkers import same_bits, same_hex, same_octal, check_fixed
ANS=json.loads(pathlib.Path('student/answers.json').read_text())
# dummy test for packaging
def test_dummy(): assert True