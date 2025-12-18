"""
QUESTION:
Extract the integer value from a given string. The input string is guaranteed to contain at least one integer. Write a function named `extract_integer` that takes a string as input and returns the integer value as output.
"""

import re

def extract_integer(s):
    """
    Extracts the integer value from a given string.

    Args:
    s (str): The input string containing at least one integer.

    Returns:
    int: The extracted integer value.
    """
    return int(re.search(r'\d+', s).group(0))