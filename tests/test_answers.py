
import json
from pathlib import Path
from utils.checkers import same_bits, same_hex, same_oct, check_fixed

ANS = json.loads(Path('student/answers.json').read_text())

EXP = {
    "conv.dec156.bin":"10011100", "conv.dec156.oct":"234", "conv.dec156.hex":"9C",
    "conv.bin101101.dec":45, "conv.bin101101.oct":"55", "conv.bin101101.hex":"2D",
    "conv.oct745.dec":485, "conv.oct745.bin":"111100101", "conv.oct745.hex":"1E5",
    "conv.hex3F9.dec":1017, "conv.hex3F9.bin":"1111111001", "conv.hex3F9.oct":"1771",
    "add.1011+1101":"11000", "add.100110+101011":"1001001", "add.11101+10111":"110100",
    "sub.1101-1010":"11", "sub.10110-1001":"1101", "sub.10001-1110":"11",
    "twos.101010":"010110", "twos.110011":"001101", "twos.1001":"0111",
    "fx.12.75.i4f4":"1100.1100", "fx.5.125.i3f5":"101.00100", "fx.7.5.i4f4":"0111.1000",
    "lim.unsigned8.max":255, "lim.signed8.max":127, "lim.signed8.min":-128
}

# 27 Assertions = 27 points

def test_conversions():
    assert same_bits(EXP["conv.dec156.bin"], ANS["conv.dec156.bin"])
    assert same_oct (EXP["conv.dec156.oct"], ANS["conv.dec156.oct"])
    assert same_hex(EXP["conv.dec156.hex"], ANS["conv.dec156.hex"])

    assert ANS["conv.bin101101.dec"] == EXP["conv.bin101101.dec"]
    assert same_oct (EXP["conv.bin101101.oct"], ANS["conv.bin101101.oct"])
    assert same_hex(EXP["conv.bin101101.hex"], ANS["conv.bin101101.hex"])

    assert ANS["conv.oct745.dec"] == EXP["conv.oct745.dec"]
    assert same_bits(EXP["conv.oct745.bin"], ANS["conv.oct745.bin"])
    assert same_hex(EXP["conv.oct745.hex"], ANS["conv.oct745.hex"])

    assert ANS["conv.hex3F9.dec"] == EXP["conv.hex3F9.dec"]
    assert same_bits(EXP["conv.hex3F9.bin"], ANS["conv.hex3F9.bin"])
    assert same_oct (EXP["conv.hex3F9.oct"], ANS["conv.hex3F9.oct"])

def test_addition():
    assert same_bits(EXP["add.1011+1101"], ANS["add.1011+1101"])
    assert same_bits(EXP["add.100110+101011"], ANS["add.100110+101011"])
    assert same_bits(EXP["add.11101+10111"], ANS["add.11101+10111"])

def test_subtraction():
    assert same_bits(EXP["sub.1101-1010"], ANS["sub.1101-1010"])
    assert same_bits(EXP["sub.10110-1001"], ANS["sub.10110-1001"])
    assert same_bits(EXP["sub.10001-1110"], ANS["sub.10001-1110"])

def test_twos():
    assert same_bits(EXP["twos.101010"], ANS["twos.101010"])
    assert same_bits(EXP["twos.110011"], ANS["twos.110011"])
    assert same_bits(EXP["twos.1001"], ANS["twos.1001"])

def test_fixed():
    assert check_fixed(EXP["fx.12.75.i4f4"], ANS["fx.12.75.i4f4"])
    assert check_fixed(EXP["fx.5.125.i3f5"], ANS["fx.5.125.i3f5"])
    assert check_fixed(EXP["fx.7.5.i4f4"], ANS["fx.7.5.i4f4"])

def test_limits():
    assert ANS["lim.unsigned8.max"] == EXP["lim.unsigned8.max"]
    assert ANS["lim.signed8.max"] == EXP["lim.signed8.max"]
    assert ANS["lim.signed8.min"] == EXP["lim.signed8.min"]
