"""
QUESTION:
Create a function named `match_string` that uses a regular expression to match any string that starts with "dog", followed by zero or more uppercase letters, and ends with the character "X". The function should return `True` if the input string matches this pattern and `False` otherwise.
"""

import re

def match_string(input_string):
    # Regular expression pattern
    pattern = r'^dog[A-Z]*X$'
    if re.match(pattern, input_string):
        return True
    else:
        return False