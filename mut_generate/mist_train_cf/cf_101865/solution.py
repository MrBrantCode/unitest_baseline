"""
QUESTION:
Write a function `normalize_string` that takes a string as input, removes all non-alphanumeric characters, and converts the remaining characters to lowercase while preserving their original order.
"""

import re

def normalize_string(input_string):
    """
    This function takes a string as input, removes all non-alphanumeric characters, 
    and converts the remaining characters to lowercase while preserving their original order.

    Args:
    input_string (str): The input string to be normalized.

    Returns:
    str: The normalized string.
    """
    normalized_string = re.sub(r'[^a-zA-Z0-9]', '', input_string)
    normalized_string = normalized_string.lower()
    return normalized_string