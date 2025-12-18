"""
QUESTION:
Write a function that extracts all numbers larger than 0 from a given string using regex. The function should return a list of integers. The numbers can be of any length and may be embedded within the string.
"""

import re

def extract_positive_numbers(input_string):
    """
    Extracts all positive integers from a given string using regex.

    Args:
        input_string (str): The string from which to extract numbers.

    Returns:
        list: A list of integers larger than 0.
    """
    return [int(num) for num in re.findall(r'\b[1-9][0-9]*\b', input_string)]