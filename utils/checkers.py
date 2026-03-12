import re
def norm_bits(s): return re.sub(r'[_\s]','',str(s).strip())
def same_bits(e,g): return norm_bits(e)==norm_bits(g)
def same_hex(e,g): return norm_bits(e.upper())==norm_bits(str(g).upper())
def same_octal(e,g): return norm_bits(e)==norm_bits(g)
def check_fixed(e,g): return norm_bits(e)==norm_bits(g)