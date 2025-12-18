"""
QUESTION:
Design a function `match_red_apple` that takes a string as input and returns True if the word "apple" is found preceded by "red" and followed by a comma, ignoring occurrences within quotes.
"""

import re

def match_red_apple(input_string):
    pattern = r'\bred\b\s+(?:(?!\b"[^"]*"\b)[^,])*\s+apple\b(?=,)'
    return bool(re.search(pattern, input_string))