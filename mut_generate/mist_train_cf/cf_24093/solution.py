"""
QUESTION:
Create a function `match_float` that uses a regular expression to match a string as a positive or negative floating-point number. The function should return a boolean indicating whether the input string is a valid floating-point number. The function should consider both positive and negative numbers, with or without decimal points.
"""

import re

def match_float(s):
    pattern = r"(-?\d*\.\d+)|(-?\d+\.\d*)"
    return bool(re.fullmatch(pattern, s))