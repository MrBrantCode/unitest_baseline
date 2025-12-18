"""
QUESTION:
Write a function `matches_pattern(s)` that takes a string `s` as input and returns `True` if the string contains only the letters 'a' and 'b' and follows the pattern where any 'a' characters must be followed by at least twice the number of consecutive 'b' characters.
"""

import re

def matches_pattern(s):
    return re.fullmatch(r'(a{1}b{2})*', s) is not None