"""
QUESTION:
Compose a function called `is_digits_only` that takes a string as input and returns `True` if the string consists only of numerical digits and `False` otherwise, using a regular expression.
"""

import re

def is_digits_only(s):
    pattern = '^[0-9]+$'
    return bool(re.match(pattern, s))