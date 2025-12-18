"""
QUESTION:
Create a function called `extract_phone_numbers` that takes a string as input and returns all telephone numbers in the format XXX-XXX-XXXX, where X is a digit. The function should use regular expressions and return the numbers as a list.
"""

import re

def extract_phone_numbers(s):
    """
    Extracts all telephone numbers in the format XXX-XXX-XXXX from a string.
    
    Args:
        s (str): The input string.
    
    Returns:
        list: A list of telephone numbers.
    """
    return re.findall(r'\d{3}-\d{3}-\d{4}', s)