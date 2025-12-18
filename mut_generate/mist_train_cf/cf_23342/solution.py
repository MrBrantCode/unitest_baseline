"""
QUESTION:
Create a function called `remove_special_chars_and_whitespace` that takes a string as input, removes all non-word characters (special characters) and all whitespace from the string, and returns the resulting string.
"""

import re

def remove_special_chars_and_whitespace(s):
    return re.sub(r'\s','', re.sub(r'[^\w\s]','', s))