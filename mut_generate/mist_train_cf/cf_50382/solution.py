"""
QUESTION:
Create a function named `is_numeric_string(s)` that takes a string `s` as input and returns a boolean value indicating whether the string consists solely of numerical characters. The function should return True if all characters in the string are digits and False otherwise.
"""

import re

def is_numeric_string(s):
    return bool(re.match('^[0-9]+$', s))