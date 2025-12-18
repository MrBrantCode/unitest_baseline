"""
QUESTION:
Write a function `is_valid(s)` that takes a string `s` as input and returns `True` if the string is alphanumeric (including Unicode characters), contains at least one letter, and contains at least one digit. The function should return `False` otherwise.
"""

import re

def is_valid(s):
    pattern = re.compile(r'^(?=.*[a-zA-Z\u0080-\uFFFF])(?=.*[0-9]).+$')
    return bool(pattern.match(s))