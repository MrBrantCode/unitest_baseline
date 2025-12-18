"""
QUESTION:
Write a function called `remove_leading_pattern` that takes a string `s` and a pattern `p` as input, and returns the string `s` with the pattern `p` removed from the beginning of each line. The function should handle strings with multiple lines correctly.
"""

import re

def remove_leading_pattern(s, p):
    return re.sub('^' + p, '', s, flags=re.MULTILINE)