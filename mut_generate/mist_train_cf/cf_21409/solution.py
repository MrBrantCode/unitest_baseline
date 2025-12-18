"""
QUESTION:
Write a function `find_capital_n_words` that takes a string as input and returns a list of all words that start with a capital letter and end with "n", and do not contain any numbers or special characters.
"""

import re

def find_capital_n_words(text):
    """
    This function takes a string as input and returns a list of all words 
    that start with a capital letter and end with "n", and do not contain 
    any numbers or special characters.

    Args:
    text (str): Input string

    Returns:
    list: List of words that meet the specified conditions
    """
    pattern = r"\b[A-Z][a-zA-Z]*n\b"
    return re.findall(pattern, text)