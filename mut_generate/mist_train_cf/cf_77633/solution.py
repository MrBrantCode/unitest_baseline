"""
QUESTION:
Create a function `check_pattern(string)` that takes a string as input and returns `True` if the string starts with a non-alphanumeric character, followed by exactly three lowercase letters, and ends with a numerical sequence of two to four digits, and `False` otherwise.
"""

import re

def check_pattern(string):
    pattern = r'^\W[a-z]{3}\d{2,4}$'
    return bool(re.match(pattern, string))