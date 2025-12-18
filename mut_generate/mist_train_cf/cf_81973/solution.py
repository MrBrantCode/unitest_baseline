"""
QUESTION:
Write a function `check_string` that takes a string `s` as input and returns `True` if the string contains only letters (a-z, A-Z) and spaces, and `False` otherwise. The string may contain one or more spaces, but must not contain any digits or special characters.
"""

import re
pattern = r'^[a-zA-Z ]+$'

def check_string(s):
    if re.match(pattern, s):
        return True
    else:
        return False