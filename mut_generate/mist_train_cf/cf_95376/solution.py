"""
QUESTION:
Write a function `get_words(sentence)` that takes a sentence as input and returns a list of words that do not contain vowels and have a length of 5 characters or less.
"""

import re

def get_words(sentence):
    pattern = r'\b(?![aeiouAEIOU])[a-zA-Z]{1,5}\b'
    return re.findall(pattern, sentence)