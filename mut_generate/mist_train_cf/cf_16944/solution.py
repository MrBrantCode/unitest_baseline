"""
QUESTION:
Write a function called `convert_to_words` that takes a string of text as input, and returns a list of words separated by whitespace. The function should ignore punctuation marks, but include numbers and words separated by a hyphen or an apostrophe.
"""

import re

def convert_to_words(text):
    """
    This function takes a string of text as input, and returns a list of words 
    separated by whitespace. The function ignores punctuation marks, but includes 
    numbers and words separated by a hyphen or an apostrophe.

    Args:
        text (str): The input string.

    Returns:
        list: A list of words.
    """
    return re.findall(r"\w[\w'-]*", text)