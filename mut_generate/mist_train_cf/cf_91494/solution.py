"""
QUESTION:
Design a function named `split_sentence` that takes a sentence as input, splits it into words while treating punctuation and special characters as separate words, and returns the resulting list of words. The function should correctly handle punctuation and special characters.
"""

import re

def split_sentence(sentence):
    words = re.findall(r'\w+|[^\w\s]', sentence)
    return words