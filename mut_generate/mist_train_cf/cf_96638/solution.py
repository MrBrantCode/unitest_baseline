"""
QUESTION:
Create a function `get_unique_words` that takes a sentence as input. The function should return a list of unique words from the sentence in alphabetical order, ignoring case, punctuation marks, special characters, and numbers. The input sentence can contain any of these characters and should be handled accordingly.
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