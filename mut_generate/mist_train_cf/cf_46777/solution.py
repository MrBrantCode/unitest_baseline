"""
QUESTION:
Create a function `check_congruity(string1, string2)` that determines if two input strings `string1` and `string2` both consist of one or more lowercase alphabetical characters. The function should return `True` if both strings match this criteria and `False` otherwise.
"""

import re

def check_congruity(string1, string2):
    pattern = re.compile(r'^[a-z]+$')
    return bool(pattern.match(string1)) and bool(pattern.match(string2))