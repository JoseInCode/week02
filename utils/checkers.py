
import re

def norm(s):
    # remove spaces, underscores, newlines and tabs; keep dots
    return re.sub("[ _
	]", "", str(s)).strip()

def same_bits(exp, got):
    return norm(exp) == norm(got)

def same_hex(exp, got):
    return norm(exp).upper() == norm(got).upper()

def same_oct(exp, got):
    return norm(exp) == norm(got)

def check_fixed(exp, got):
    # strict dotted format
    return norm(exp) == norm(got)
