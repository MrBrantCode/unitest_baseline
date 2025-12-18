"""
QUESTION:
Create a function named `get_unique_words` that takes a string `sentence` as input, removes any non-alphabetic characters and converts to lowercase, splits it into a list of words, removes duplicates while preserving order is not required, and returns the list in alphabetical order.
"""

import re

def get_unique_words(sentence):
    # Remove punctuation marks, special characters, and numbers
    sentence = re.sub(r'[^\w\s]', '', sentence)
    # Split the sentence into a list of words
    words = sentence.lower().split()
    # Remove duplicate words
    unique_words = list(set(words))
    # Sort the list of unique words in alphabetical order
    unique_words.sort()
    return unique_words