"""
QUESTION:
Develop a function named "get_string" that accepts a string "text" as an argument. The function should remove all non-alphanumeric characters except spaces from the input string, split the resulting string into individual words, and then concatenate them using underscores to create a single string. The function must be able to handle strings of arbitrary length.
"""

import re
def get_string(text):
    # remove all non-alphanumeric characters except spaces
    text = re.sub(r'[^\w\s]', '', text)
    # split the text into individual words
    words = text.split()
    # concatenate the words using underscores
    return '_'.join(words)