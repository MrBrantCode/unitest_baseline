"""
QUESTION:
Write a function `find_long_capitalized_words` that takes a sentence as input and returns a list of words that start with a capital letter and have at least 7 characters. The function should use a RegEx pattern to match the words.
"""

import re

def find_long_capitalized_words(sentence):
    """
    This function takes a sentence as input and returns a list of words that start with a capital letter and have at least 7 characters.

    Args:
        sentence (str): The input sentence.

    Returns:
        list: A list of words that start with a capital letter and have at least 7 characters.
    """
    pattern = r"\b[A-Z][A-Za-z]{6,}\b"
    return re.findall(pattern, sentence)