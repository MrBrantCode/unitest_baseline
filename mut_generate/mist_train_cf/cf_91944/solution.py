"""
QUESTION:
Create a regular expression function `validate_string` to match a string that contains a number followed by a letter and is at least 6 characters long, using only alphanumeric characters (a-z, A-Z, 0-9). The function should return `True` if the string matches the pattern and `False` otherwise.
"""

import re

def validate_string(s):
    pattern = r'^(?=.*\d)[a-zA-Z0-9]{6,}$'
    return bool(re.match(pattern, s))