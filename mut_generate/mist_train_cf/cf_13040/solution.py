"""
QUESTION:
Create a function, `match_string`, that uses a regular expression to match only strings that start with the letter 'A' and end with a digit between 1 and 5 (inclusive). The function should return True if the string matches the pattern, and False otherwise.
"""

import re

def match_string(s):
    pattern = r'^A.*[1-5]$'
    return bool(re.match(pattern, s))