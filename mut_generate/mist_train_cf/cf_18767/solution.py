"""
QUESTION:
Write a regular expression for a function `match_string` that returns true if a string contains any number of digits but does not contain any non-digit characters at the end. The regular expression should not match any string that contains non-digit characters before the first digit. The string can start with zero or more non-digit characters.
"""

import re

def match_string(s):
    pattern = r'^\D*\d+\D*$'
    return bool(re.match(pattern, s))