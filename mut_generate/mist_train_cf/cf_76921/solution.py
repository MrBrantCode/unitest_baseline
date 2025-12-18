"""
QUESTION:
Create a function called `match_pattern` that returns `True` if the input string starts with "DOG", contains only uppercase letters, and ends with "X", and `False` otherwise.
"""

import re

def match_pattern(text):
    pattern = "^DOG[A-Z]*X$"
    return bool(re.search(pattern, text))