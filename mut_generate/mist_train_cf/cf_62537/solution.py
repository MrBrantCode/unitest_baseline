"""
QUESTION:
Design a function `match_pattern(string)` that takes a string as input and returns `True` if the string matches the pattern of one or more octal digits followed by an uppercase consonant (a letter that is not A, E, I, O, U), and `False` otherwise.
"""

import re

def match_pattern(string):
    pattern = r'^[0-7]+[B-DF-HJ-NP-TV-Z]$'
    return bool(re.match(pattern, string))