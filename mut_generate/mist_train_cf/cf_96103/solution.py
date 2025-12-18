"""
QUESTION:
Design a function `get_unique_words(sentence)` that takes a sentence as input and returns a list of unique words. The function should ignore punctuation marks, consider words in a case-insensitive manner, and not contain any duplicate words.
"""

import re

def get_unique_words(sentence):
    sentence = re.sub(r'[^\w\s]', '', sentence.lower())
    words = sentence.split()
    unique_words = set(words)
    return list(unique_words)