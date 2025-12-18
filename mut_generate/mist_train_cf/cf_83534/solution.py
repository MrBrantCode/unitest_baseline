"""
QUESTION:
Write a function `extract_numbers` that takes a string as input and returns a list of numerical values found in the string. The numerical values can be integers or decimal numbers, and they may appear anywhere in the string. The function should return the numbers as strings, in the order they appear in the input string.
"""

import re

def extract_numbers(text):
    """
    Extract numerical values from a string.

    Args:
    text (str): Input string to search for numbers.

    Returns:
    list: A list of numerical values found in the string.
    """
    pattern = r'[0-9]+\.?[0-9]*'
    return re.findall(pattern, text)