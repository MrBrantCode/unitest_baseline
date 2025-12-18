"""
QUESTION:
Write a function called `find_cat_digit` that takes a string as input and returns all occurrences of the substring "cat" followed by a digit. The function must use a regex pattern to match the substring and a digit. The digit can be any number from 0 to 9.
"""

import re

def find_cat_digit(string):
    """
    This function takes a string as input and returns all occurrences of the substring "cat" followed by a digit.

    Args:
        string (str): The input string to search for the pattern.

    Returns:
        list: A list of all occurrences of the substring "cat" followed by a digit.
    """
    return re.findall(r"cat\d", string)