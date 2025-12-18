"""
QUESTION:
Create a function `float_pattern` that uses regular expression to match both positive and negative floating-point numerals. The function should consider an optional sign and decimals. The input string should match the pattern entirely.
"""

import re

def float_pattern(s):
    pattern = r"^[-+]?\d*\.\d+$|^[-+]?\d+$"
    return bool(re.fullmatch(pattern, s))