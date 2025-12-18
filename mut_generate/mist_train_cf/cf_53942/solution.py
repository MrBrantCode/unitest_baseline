"""
QUESTION:
Write a function `validate_digits` that takes a string as input and returns `True` if the string consists only of numerical digits, and `False` otherwise.
"""

import re

def validate_digits(s):
    return bool(re.match('^[0-9]+$', s))