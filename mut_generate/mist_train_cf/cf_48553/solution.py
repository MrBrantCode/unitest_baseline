"""
QUESTION:
Create a function `get_unique_words(sentence)` that takes a string sentence as input and returns a set of unique words. The function should disregard punctuation and special characters, and treat the same word in different cases as the same word.
"""

import re

def get_unique_words(sentence):
    # find all words and make them lower case
    words = re.findall(r'\w+', sentence.lower())
    # return only unique words
    return set(words)