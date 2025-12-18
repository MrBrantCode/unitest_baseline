"""
QUESTION:
Write a function called find_pattern that uses a regular expression to identify a character sequence of arbitrary length that culminates in the consecutive letters "o" and "o". The function should return whether the pattern is found in a given text.
"""

import re

def find_pattern(text):
    pattern = '.*oo'
    return True if re.search(pattern, text) else False