"""
QUESTION:
Create a function `find_alphanumeric_digits` that takes a string as input and returns all occurrences of alphanumeric characters that are immediately followed by exactly three digits. The function should only match whole words, where a word is defined as a sequence of alphanumeric characters separated by non-alphanumeric characters.
"""

import re

def find_alphanumeric_digits(text):
    """
    Returns all occurrences of alphanumeric characters that are immediately 
    followed by exactly three digits in the given text.

    Args:
    text (str): The input string to search for patterns.

    Returns:
    list: A list of strings where each string contains an alphanumeric character 
          followed by exactly three digits.
    """
    pattern = r"\b\w{1}\d{3}\b"
    return re.findall(pattern, text)