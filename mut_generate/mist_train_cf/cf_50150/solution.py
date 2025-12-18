"""
QUESTION:
Create a function called `match_string(s)` that takes a string `s` as input and returns `True` if the string starts with two consecutive "#" symbols followed by exactly four alphabetic characters, and `False` otherwise. The function should use regular expressions to match the pattern.
"""

import re

def match_string(s):
    pattern = "##[A-Za-z]{4}"
    return bool(re.fullmatch(pattern, s))