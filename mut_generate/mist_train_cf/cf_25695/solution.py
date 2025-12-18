"""
QUESTION:
Write a function named `verify_pattern` that takes a string as input and returns `True` if the string matches the pattern of one or more digits followed by a hyphen followed by one or more digits, and `False` otherwise.
"""

import re

def verify_pattern(s):
    exp = re.compile("\d+-\d+")
    return bool(exp.fullmatch(s))