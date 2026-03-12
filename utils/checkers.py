
import re

def norm(s):
    return re.sub(r"[ _
	]", "", str(s)).strip()

def same_bits(exp, got):
    return norm(exp) == norm(got)

def same_hex(exp, got):
    return norm(exp).upper() == norm(got).upper()

def same_oct(exp, got):
    return norm(exp) == norm(got)

def check_fixed(exp, got):
    # Strict dotted format
    return norm(exp) == norm(got)
