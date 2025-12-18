"""
QUESTION:
Create a function that uses a regular expression to match the standalone words 'beginning' and 'starting' in a given string, regardless of case. The function should not match if the words are part of a larger word or are preceded/followed by any letters or numbers. The function should return a list of all matches.
"""

import re

def entrance(s):
    pattern = r'\b(?:beginning|starting)\b'
    return re.findall(pattern, s, re.IGNORECASE)