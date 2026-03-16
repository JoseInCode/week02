import re

def norm(s):
    # Remove spaces, underscores, newlines, tabs
    return re.sub("[ _\\n\\t]", "", str(s)).strip()

def same_bits(exp, got):
    return norm(exp) == norm(got)

def same_hex(exp, got):
    return norm(exp).upper() == norm(got).upper()

def same_oct(exp, got):
    return norm(exp) == norm(got)

def check_fixed(exp, got):
    # Strict dotted format for fixed point
    return norm(exp) == norm(got)