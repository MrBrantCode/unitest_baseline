"""
QUESTION:
Create a function `find_word_indices` that takes a string `text` and a string `word` as input and returns a list of tuples, where each tuple contains the starting and ending indices of `word` in `text`. The search should be case-insensitive and ignore special characters and whitespace. The function should return all instances of `word` in `text`.
"""

import re

def find_word_indices(text, word):
    word_pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
    matches = [(m.start(0), m.end(0)) for m in re.finditer(word_pattern, text)]
    
    return matches