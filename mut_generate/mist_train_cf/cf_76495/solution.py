"""
QUESTION:
Create a function named `is_uppercase_or_digits` that takes a string `s` as input and returns `True` if the string consists solely of uppercase English alphabets and numerical digits, and `False` otherwise. The function should match the entire string and not just a part of it.
"""

import re

def is_uppercase_or_digits(s):
    pattern = "^[A-Z0-9]+$"
    return bool(re.match(pattern, s))