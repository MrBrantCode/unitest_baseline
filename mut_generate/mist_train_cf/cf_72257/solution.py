"""
QUESTION:
Create a function `match_string(s)` that takes a string `s` as input and returns `True` if the string contains exactly two uppercase letters followed by exactly three numbers and ends with exactly one lowercase letter, and `False` otherwise.
"""

import re

def match_string(s):
    pattern = '^[A-Z]{2}\d{3}[a-z]$'
    return bool(re.match(pattern, s))