"""
QUESTION:
Create a function `is_numeric` that takes a string as input and returns `True` if the string contains only numerical values and `False` otherwise. The function should use regular expressions to validate the input.
"""

import re

def is_numeric(s):
    return bool(re.match('^[0-9]+$', s))