"""
QUESTION:
Write a function named `find_numbers_starting_with_8` that takes a string `text` as input and returns a list of all numerical values starting specifically with the integer 8, excluding any numbers with non-numerical values immediately following the 8.
"""

import re

def find_numbers_starting_with_8(text):
    """
    This function takes a string as input and returns a list of all numerical values starting specifically with the integer 8, 
    excluding any numbers with non-numerical values immediately following the 8.
    
    Parameters:
    text (str): Input string containing numerical values
    
    Returns:
    list: A list of numerical values starting with 8
    """
    pattern = r'\b[8]\d*\b'
    return re.findall(pattern, text)