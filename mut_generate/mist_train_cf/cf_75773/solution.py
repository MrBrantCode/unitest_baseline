"""
QUESTION:
Write a function `extract(sentence)` that takes a string `sentence` as input, extracts all alphanumeric characters, and identifies unique words in a case-insensitive manner, ignoring punctuation and special symbols. The function should return two lists: one containing the alphanumeric characters and the other containing the unique words.
"""

import re

def extract(sentence):
    # Extract alphanumeric characters
    alphanumeric = re.findall('\w', sentence)

    # Extract words
    words = re.findall('\w+', sentence.lower())
    
    # Identify unique words
    unique_words = list(set(words))

    return alphanumeric, unique_words