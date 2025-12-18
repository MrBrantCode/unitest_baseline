"""
QUESTION:
Design a function `is_uppercase_numeric_chain(s)` that takes a string `s` as input and returns `True` if the string consists only of uppercase alphabetic characters and numerical figures, and `False` otherwise.
"""

import re

def is_uppercase_numeric_chain(s):
    pattern = r"^[A-Z0-9]+$"
    return bool(re.match(pattern, s))