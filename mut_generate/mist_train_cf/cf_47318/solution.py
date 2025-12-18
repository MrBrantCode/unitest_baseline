"""
QUESTION:
Create a function `check_string(s)` that takes a string `s` as a parameter and returns `True` if the string contains at least one numeric character and at least one uppercase alphabetic letter, and `False` otherwise.
"""

import re

def check_string(s):
    return bool(re.search(r'^(?=.*[A-Z])(?=.*\d)', s))