"""
QUESTION:
Create a function `match_string(s)` that takes a string `s` as input and returns `True` if the string contains exactly two uppercase letters followed by three unique digits and ends with one lowercase letter, and `False` otherwise. The string length must be exactly six characters long.
"""

import re

def match_string(s):
    pattern = r"^[A-Z]{2}[0-9]{3}[a-z]$"
    if re.match(pattern, s):
        if len(set(s[2:5])) == 3: 
            return True
    return False