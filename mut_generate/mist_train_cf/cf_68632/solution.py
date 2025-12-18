"""
QUESTION:
Write a function named `has_pattern` that takes a string `s` as input and returns `True` if the string contains the sequence 'abbb' and `False` otherwise.
"""

import re

def has_pattern(s):
    return bool(re.search('abbb', s))