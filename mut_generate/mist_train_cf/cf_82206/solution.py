"""
QUESTION:
Create a function called `detect_pattern` that uses a regular expression to determine if a given string starts with the character '1' and ends with the character '@'.
"""

import re

def detect_pattern(text):
    pattern = '^1.*@$'
    return bool(re.search(pattern, text))