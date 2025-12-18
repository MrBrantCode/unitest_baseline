"""
QUESTION:
Write a function `match_pattern` that uses a regex pattern to match all words in a string that start with a lowercase letter, have at least one uppercase letter in the middle, and end with an uppercase letter.
"""

import re

def match_pattern(s):
    return re.findall(r'\b[a-z][a-zA-Z]*[A-Z]\b', s)