"""
QUESTION:
Develop a function named "get_string" that takes a string "text" as input. The function should remove all non-alphanumeric characters except spaces from the string, split the resulting string into individual words, and then concatenate these words using underscores into a single string. The function should be able to handle strings of arbitrary length and return the resulting string.
"""

import re

def get_string(text):
    # remove all non-alphanumeric characters except spaces
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # split the text into individual words
    words = text.split()
    # concatenate the words using underscores
    return '_'.join(words)