"""
QUESTION:
Create a function named `check_string` that takes a string as input and returns `True` if the string's length is above 10, contains at least two numbers, and the last character is not alphanumeric; otherwise, return `False`.
"""

import re

def check_string(s):
    if len(s) > 10 and re.search(r'\d.*\d', s) and not s[-1].isalnum():
        return True
    else:
        return False