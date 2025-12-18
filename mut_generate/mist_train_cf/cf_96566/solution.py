"""
QUESTION:
Write a function `find_words` that takes a string `text` as input and returns a list of words that start with a capital letter and end with "n", and do not contain any numbers or special characters. The function should use regular expression to find the matching words.
"""

import re

def find_words(text):
    """
    This function finds all words in the input text that start with a capital letter and end with "n", 
    and do not contain any numbers or special characters.

    Args:
        text (str): The input text to search for words.

    Returns:
        list: A list of words that match the specified pattern.
    """
    pattern = r"\b[A-Z][a-zA-Z]*n\b"
    return re.findall(pattern, text)