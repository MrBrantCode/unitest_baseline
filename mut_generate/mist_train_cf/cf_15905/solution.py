"""
QUESTION:
Write a Python function `count_unique_words(sentence)` that takes a string as input, ignores any punctuation marks or special characters, and returns the count of unique words in the sentence.
"""

import string

def count_unique_words(sentence):
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    words = sentence.split()
    unique_words = set(words)
    return len(unique_words)