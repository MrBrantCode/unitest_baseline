"""
QUESTION:
Create a function named `match_substrings` that takes a string as input and returns `True` if the string starts with "abcd" and ends with "efgh" (ignoring case and allowing any amount of whitespace in between "abcd" and "efgh"), and `False` otherwise.
"""

import re

def match_substrings(text):
    pattern = re.compile(r'abcd\s*.*\s*efgh$', re.IGNORECASE)
    match = pattern.match(text)
    if match:
        return True
    else:
        return False