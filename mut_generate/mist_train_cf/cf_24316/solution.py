"""
QUESTION:
Create a function called `match_numbers_starting_with_8` that takes a string as input and returns True if the string represents a number that starts with 8, and False otherwise. The input string is assumed to contain only digits.
"""

import re

def match_numbers_starting_with_8(s):
    return bool(re.match('^8\d+$', s))