"""
QUESTION:
Create a function `is_string_numerical(s)` that takes a string `s` as input and returns `True` if the string consists exclusively of numerical digits and `False` otherwise.
"""

import re

def is_string_numerical(s):
    pattern = re.compile(r'^\d+$')
    return bool(pattern.match(s))