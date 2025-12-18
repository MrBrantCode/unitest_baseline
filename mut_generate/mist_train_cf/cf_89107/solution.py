"""
QUESTION:
Design a function named `get_unique_words` that takes a sentence as input and returns an array of unique words. The function should ignore punctuation marks, consider words in a case-insensitive manner, and handle sentences with up to 10,000 words efficiently. The returned array should not contain any duplicate words.
"""

import re

def get_unique_words(sentence):
    # Remove punctuation marks, convert to lowercase, and split into words
    words = re.sub(r'[^\w\s]', '', sentence).lower().split()

    # Return an array of unique words using a set
    return list(set(words))