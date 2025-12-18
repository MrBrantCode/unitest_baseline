"""
QUESTION:
Construct a function `find_cat_words(text)` that takes a string as input and returns a list of all words that start with 'cat' (case-insensitive), including instances where 'cat' appears immediately after punctuation marks.
"""

import re

def find_cat_words(text):
    pattern = r"(?:(?<=\W)|\b)(cat\w*)"
    matches = re.findall(pattern, text, re.IGNORECASE)
    return matches