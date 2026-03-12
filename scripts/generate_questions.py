
#!/usr/bin/env python3
import os, json, random, argparse, hashlib
from pathlib import Path

def seed_from_text(text: str):
    h = hashlib.sha256(text.encode('utf-8')).hexdigest()
    return int(h[:16], 16)

def gen_decimal(low=32, high=1023):
    return random.randint(low, high)

def gen_binary(min_bits=4, max_bits=7):
    n = random.randint(min_bits, max_bits)
    return format(random.randint(0, (1<<n)-1), f"0{n}b")

def gen_octal(digits=3):
    # ensure no leading zero unless zero itself
    n = random.randint(1, (8**digits)-1)
    return format(n, 'o')

def gen_hex(digits=3):
    n = random.randint(1, (16**digits)-1)
    return format(n, 'X')

def ensure_sub_pair(min_bits=4, max_bits=7):
    a = int(gen_binary(min_bits, max_bits), 2)
    b = int(gen_binary(min_bits, max_bits), 2)
    if a < b:
        a, b = b, a
    return format(a, 'b'), format(b, 'b')

def twos_of(bstr: str):
    n = len(bstr)
    x = int(bstr, 2)
    return format((1<<n) - x, f"0{n}b")

def gen_fixed(I, F):
    # build an exactly representable value with I integer bits and F fractional bits
    max_int = (1<<I) - 1
    int_part = random.randint(0, max_int)
    frac_bits = ''.join(random.choice('01') for _ in range(F))
    frac_val = sum((1 if c=='1' else 0) * (2**-(i+1)) for i, c in enumerate(frac_bits))
    x = int_part + frac_val
    # Pretty decimal string (avoid float noise)
    dec = int_part + sum((1 if c=='1' else 0) * (1/(2**(i+1))) for i,c in enumerate(frac_bits))
    # format decimal with up to 6 places, strip trailing zeros
    x_str = ("%.6f" % dec).rstrip('0').rstrip('.')
    return {"x": x_str, "I": I, "F": F, "bits": f"{int_part:0{I}b}.{frac_bits}"}

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--seed', default=None)
    args = p.parse_args()
    seed_text = args.seed or os.getenv('GITHUB_ACTOR') or 'local-default-seed'
    random.seed(seed_from_text(seed_text))

    spec = {}
    # Conversions
    spec['conv'] = {
        'dec': gen_decimal(32, 1023),
        'bin': gen_binary(5, 8),
        'oct': gen_octal(3),
        'hex': gen_hex(3)
    }
    # Addition pairs
    spec['add'] = [ [gen_binary(4,7), gen_binary(4,7)] for _ in range(3) ]
    # Subtraction pairs (minuend >= subtrahend)
    spec['sub'] = [ list(ensure_sub_pair(4,7)) for _ in range(3) ]
    # Two's complement inputs (4..8 bits)
    spec['twos'] = [ gen_binary(4,8) for _ in range(3) ]
    # Fixed point (random but representable)
    spec['fixed'] = [ gen_fixed(4,4), gen_fixed(3,5), gen_fixed(4,4) ]
    # Limits
    spec['limits'] = { 'bits': 8 }

    # save spec
    Path('meta').mkdir(parents=True, exist_ok=True)
    Path('questions').mkdir(parents=True, exist_ok=True)
    with open('meta/generated_spec.json','w',encoding='utf-8') as f:
        json.dump(spec, f, indent=2)

    # build student-visible markdown
    md = [
        '# Personalised Questions',
        '',
        '## 1) Number Conversion',
        f"Convert **decimal {spec['conv']['dec']}** to: binary, octal, hex.",
        f"Convert **binary {spec['conv']['bin']}** to: decimal, octal, hex.",
        f"Convert **octal {spec['conv']['oct']}** to: decimal, binary, hex.",
        f"Convert **hex {spec['conv']['hex']}** to: decimal, binary, octal.",
        '',
        '## 2) Binary Addition',
    ]
    for i,(a,b) in enumerate(spec['add'], start=1):
        md.append(f"- add.{i}: {a} + {b}")
    md += ['', '## 3) Binary Subtraction']
    for i,(a,b) in enumerate(spec['sub'], start=1):
        md.append(f"- sub.{i}: {a} - {b}")
    md += ['', "## 4) Two's Complement"]
    for i,b in enumerate(spec['twos'], start=1):
        md.append(f"- twos.{i}: {b}")
    md += ['', '## 5) Fixed-Point (strict dotted)']
    for i,fx in enumerate(spec['fixed'], start=1):
        md.append(f"- fx.{i}: represent **{fx['x']}** with **{fx['I']} integer bits** and **{fx['F']} fractional bits**")
    md += ['', '## 6) Representation Limits (8-bit)']
    md += ['- lim.unsigned8.max', '- lim.signed8.max', '- lim.signed8.min']

    with open('questions/generated.md','w',encoding='utf-8') as f:
        f.write('
'.join(md)+"
")

if __name__ == '__main__':
    main()
