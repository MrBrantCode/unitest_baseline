"""
QUESTION:
Write a function `match_pattern` that takes a string as input and returns `True` if the string consists solely of one or more uppercase alphabetic letters and numerical digits, and `False` otherwise.
"""

import re

def match_pattern(string):
    pattern = r'^[A-Z0-9]+$'
    return bool(re.match(pattern, string))