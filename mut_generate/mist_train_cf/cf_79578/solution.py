"""
QUESTION:
Create a function named `words_with_r` that takes a string `text` as input. This function should return a list of all the words in the input string that start with the letter "r" (case insensitive) and are followed by zero or more alphanumeric characters or underscores.
"""

import re

def words_with_r(text):
    pattern = r'\br\w*\b'
    return re.findall(pattern, text, re.IGNORECASE)