"""
QUESTION:
Write a function `find_first_occurrence` that takes two parameters: `text` and `word`. The function should return the index of the first occurrence of the word in the text, handling cases where the word is followed by punctuation marks or is part of a larger word, and is case-insensitive. If the word is not found, return -1.
"""

import re

def find_first_occurrence(text, word):
    word = word.lower()
    pattern = re.compile(r'\b{}\b'.format(re.escape(word)))
    match = re.search(pattern, text.lower())
    if match:
        return match.start()
    return -1