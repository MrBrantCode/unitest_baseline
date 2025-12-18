"""
QUESTION:
Construct a regular expression pattern that matches the string "dog" followed by any number of characters, excluding the alphabetic letters "x" and "y", until the end of the string.
"""

import re

def match_dog_string(s):
    pattern = r'dog[^xy]*$'
    return bool(re.search(pattern, s))