"""
QUESTION:
Write a function `is_valid_string(s)` that takes a string `s` as input and returns `True` if the string contains any number of even digits (0, 2, 4, 6, 8) in sequence and does not contain any non-digit character or odd digit, and `False` otherwise.
"""

import re

def is_valid_string(s):
    pattern = re.compile(r'^([02468]+)$')
    return bool(pattern.match(s))