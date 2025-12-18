"""
QUESTION:
Write a function `find_words` that takes a list of words as input and returns a list of words that start with "A", end with either "e" or "s", and have a length of more than 4 characters. The function should be case-sensitive.
"""

import re

def find_words(words):
    pattern = r"\bA[a-z]*[es]\b"
    return [word for word in words if re.match(pattern, word) and len(word) > 4]