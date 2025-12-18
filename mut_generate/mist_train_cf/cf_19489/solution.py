"""
QUESTION:
Create a function `match_words` that returns a regular expression pattern matching the words 'beginning' and 'starting' in a case-insensitive manner, where the words are not preceded or followed by any letters or numbers.
"""

import re

def match_words(text):
    return bool(re.search(r'\b(?:beginning|starting)\b', text, re.IGNORECASE))