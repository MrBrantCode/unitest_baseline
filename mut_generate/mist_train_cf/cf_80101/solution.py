"""
QUESTION:
Extract all numerical figures from a given text. 

Create a function named `extract_numbers` that takes a string as input and returns a list of all numerical figures found in the string. The function should be able to identify numbers in the format of one or more decimal digits.
"""

import re

def extract_numbers(text):
    """
    Extract all numerical figures from a given text.

    Args:
        text (str): The input string.

    Returns:
        list: A list of all numerical figures found in the string.
    """
    return re.findall(r'\b\d+\b', text)