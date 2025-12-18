"""
QUESTION:
Write a function named `split_string` that takes a string `text` as input and returns a list of words. The function should split the input string into words while removing any punctuation marks. The function should use the `re` module in Python and consider word characters and whitespace as valid characters, removing any other characters from the string.
"""

import re

def split_string(text):
    # Remove punctuation marks using regex
    text = re.sub(r'[^\w\s]', '', text)

    # Split the string into words
    words = text.split()

    return words