"""
QUESTION:
Create a function `find_words` that takes two parameters: a string `text` and a character `char`. The function should use regex to find and return a list of all the words in `text` that start and end with the specified `char`. The function should match whole words only and consider words as sequences of word characters (letters, digits, or underscores).
"""

import re

def find_words(text, char):
    """
    This function takes a string `text` and a character `char` as parameters.
    It uses regex to find and return a list of all the words in `text` that start and end with the specified `char`.

    Args:
        text (str): The input text to search for words.
        char (str): The character that words should start and end with.

    Returns:
        list: A list of words that start and end with the specified `char`.
    """
    pattern = rf"\b{char}\w*{char}\b"
    return re.findall(pattern, text)