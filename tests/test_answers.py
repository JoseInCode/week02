
import json
from pathlib import Path
from utils.checkers import same_bits, same_hex, same_oct, check_fixed

# Load student answers and generated spec
ANS = json.loads(Path('student/answers.json').read_text(encoding='utf-8'))
SPEC = json.loads(Path('meta/generated_spec.json').read_text(encoding='utf-8'))

# Helpers

def to_bin(n):
    return format(n, 'b')

def to_oct(n):
    return format(n, 'o')

def to_hex(n):
    return format(n, 'X')

def bin_add(a,b):
    return format(int(a,2)+int(b,2), 'b')

def bin_sub(a,b):
    return format(int(a,2)-int(b,2), 'b')

def bits_twos(b):
    n=len(b)
    x=int(b,2)
    return format((1<<n)-x, f'0{n}b')

def fixed_bits(x_str,I,F):
    # x_str is decimal string; convert to exact binary with I.F bits
    x = float(x_str)
    int_part = int(x)
    frac = x - int_part
    # integer
    ib = format(int_part, f'0{I}b')
    # fractional
    bits = ''
    for _ in range(F):
        frac *= 2
        if frac >= 1 - 1e-12:
            bits += '1'
            frac -= 1
        else:
            bits += '0'
    return f"{ib}.{bits}"

# 1) Conversions (12 asserts)

def test_conversions():
    dec = SPEC['conv']['dec']
    b   = SPEC['conv']['bin']
    oc  = SPEC['conv']['oct']
    hx  = SPEC['conv']['hex']

    assert same_bits(to_bin(dec), ANS['conv.dec.bin'])
    assert same_oct (to_oct(dec), ANS['conv.dec.oct'])
    assert same_hex (to_hex(dec), ANS['conv.dec.hex'])

    assert int(ANS['conv.bin.dec']) == int(b,2)
    assert same_oct (to_oct(int(b,2)), ANS['conv.bin.oct'])
    assert same_hex (to_hex(int(b,2)), ANS['conv.bin.hex'])

    assert int(ANS['conv.oct.dec']) == int(oc,8)
    assert same_bits(to_bin(int(oc,8)), ANS['conv.oct.bin'])
    assert same_hex (to_hex(int(oc,8)), ANS['conv.oct.hex'])

    assert int(ANS['conv.hex.dec']) == int(hx,16)
    assert same_bits(to_bin(int(hx,16)), ANS['conv.hex.bin'])
    assert same_oct (to_oct(int(hx,16)), ANS['conv.hex.oct'])

# 2) Addition (3 asserts)

def test_addition():
    for i,(a,b) in enumerate(SPEC['add'], start=1):
        assert same_bits(bin_add(a,b), ANS[f'add.{i}'])

# 3) Subtraction (3 asserts)

def test_subtraction():
    for i,(a,b) in enumerate(SPEC['sub'], start=1):
        assert same_bits(bin_sub(a,b), ANS[f'sub.{i}'])

# 4) Two's complement (3 asserts)

def test_twos():
    for i,b in enumerate(SPEC['twos'], start=1):
        assert same_bits(bits_twos(b), ANS[f'twos.{i}'])

# 5) Fixed-point (3 asserts, strict dotted)

def test_fixed():
    for i,fx in enumerate(SPEC['fixed'], start=1):
        exp = fixed_bits(fx['x'], fx['I'], fx['F'])
        assert check_fixed(exp, ANS[f'fx.{i}'])

# 6) Limits (3 asserts)

def test_limits():
    assert ANS['lim.unsigned8.max'] == 255
    assert ANS['lim.signed8.max'] == 127
    assert ANS['lim.signed8.min'] == -128
