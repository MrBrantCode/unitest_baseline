"""
QUESTION:
Write a function `is_valid_us_telephone_num(s)` that takes a string `s` as input and returns `True` if the string contains a valid US telephone number in the format `ddd-ddd-dddd` where `d` is a digit, and `False` otherwise. The function should use regular expressions to find a standalone telephone number that is not part of another numeric sequence.
"""

import re

def is_valid_us_telephone_num(s):
    pattern = r'\b\d{3}-\d{3}-\d{4}\b'
    return bool(re.search(pattern, s))