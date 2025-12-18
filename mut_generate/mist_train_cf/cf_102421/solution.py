"""
QUESTION:
Write a function `find_first_occurrence` that finds the index of the first occurrence of a given word in a text. The function should be case-insensitive and treat the word as a whole word, ignoring occurrences where the word is part of a larger word or followed by punctuation marks. If the word is not found, return -1.
"""

import re

def find_first_occurrence(text, word):
    word = word.lower()
    pattern = re.compile(r'\b{}\b'.format(re.escape(word)))
    match = re.search(pattern, text.lower())
    if match:
        return match.start()
    return -1