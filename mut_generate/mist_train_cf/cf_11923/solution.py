"""
QUESTION:
Write a function `find_digit_start_words` that takes a string of text as input and returns a list of words that start with a digit but do not end with a digit. The function should use regular expressions to match the desired pattern. The input string can contain multiple sentences, digits, and special characters. The function should return a list of all matching words.
"""

import re

def find_digit_start_words(text):
    """
    Returns a list of words that start with a digit but do not end with a digit.

    Args:
        text (str): The input string of text.

    Returns:
        list: A list of words that match the pattern.
    """
    pattern = r'\b\d\S*[^\d\s]\b'
    return re.findall(pattern, text)