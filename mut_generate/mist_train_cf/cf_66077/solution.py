"""
QUESTION:
Create a function `match_string(s)` that returns True if the input string `s` meets the following conditions and False otherwise: 
- The string contains the semi-colon ";" symbol.
- The string does not begin or end with a whitespace.
- The string does not contain numerical digits.
"""

import re

def match_string(s):
    pattern = r'^[^0-9\s].*;.*[^0-9\s]$'
    return bool(re.match(pattern, s))