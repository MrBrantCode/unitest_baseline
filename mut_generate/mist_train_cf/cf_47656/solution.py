"""
QUESTION:
Write a function `match_expression(s: str) -> bool` that takes a string `s` as input and returns `True` if the string consists of 14-16 digits and starts with either '4' or '5', and `False` otherwise.
"""

import re

def match_expression(s: str) -> bool:
    pattern = '^[45]\d{13,15}$'
    if re.match(pattern, s):
        return True
    else:
        return False