"""
QUESTION:
Write a function `find_cat_digit` that takes a string as input and returns a list of all occurrences of the substring "cat" followed by a digit. The function should use regular expressions to search for the pattern.
"""

import re

def find_cat_digit(string):
    """
    This function takes a string as input and returns a list of all occurrences of the substring "cat" followed by a digit.
    
    Parameters:
    string (str): The input string to search for the pattern.
    
    Returns:
    list: A list of all occurrences of the substring "cat" followed by a digit.
    """
    return re.findall(r"cat\d", string)