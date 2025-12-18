"""
QUESTION:
Write a function called `find_sion_words` that takes a string as input and returns a list of words that end with 'sion'. The function should use a regular expression pattern to identify the words.
"""

import re

def find_sion_words(text):
    """
    This function finds all words in a given text that end with 'sion'.

    Args:
        text (str): The input text to search for words.

    Returns:
        list: A list of words that end with 'sion'.
    """
    pattern = r'\b\w*sion\b'
    return re.findall(pattern, text)