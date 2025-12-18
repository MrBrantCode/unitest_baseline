"""
QUESTION:
Design a function `get_unique_words(sentence)` that takes a sentence as input, removes punctuation marks, converts it to lowercase, splits it into words, and returns an array of unique words. The function should be case-insensitive, ignore punctuation marks, and handle sentences with up to 10,000 words efficiently.
"""

import re

def get_unique_words(sentence):
    sentence = re.sub(r'[^\w\s]', '', sentence)
    sentence = sentence.lower()
    words = sentence.split()
    unique_words = set(words)
    return list(unique_words)