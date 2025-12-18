"""
QUESTION:
Create a function named `clean_and_sort_string` that takes a string as input, removes all non-alphanumeric characters, and returns the resulting string sorted in alphabetical order.
"""

import re

def clean_and_sort_string(s):
    """
    This function removes all non-alphanumeric characters from the input string 
    and returns the resulting string sorted in alphabetical order.

    Args:
        s (str): The input string.

    Returns:
        str: The cleaned and sorted string.
    """
    return ''.join(sorted(re.sub('[^a-zA-Z0-9]', '', s)))