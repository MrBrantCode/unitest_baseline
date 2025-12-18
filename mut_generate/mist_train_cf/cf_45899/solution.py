"""
QUESTION:
Write a function `verify_string(s)` that takes a string `s` as input and returns `True` if it matches the following pattern and `False` otherwise: 
- starts with a non-alphanumeric and non-whitespace character
- followed by exactly 3 lowercase letters
- optionally followed by any number of uppercase letters
- ends with at least 2 but not more than 4 digits.
"""

import re

def verify_string(s):
    pattern = "^[^\w\s][a-z]{3}[A-Z]*\d{2,4}$"
    return bool(re.match(pattern, s))