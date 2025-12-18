"""
QUESTION:
Create a function named `clean_string` that takes one argument `input_string`. This function should remove all whitespace characters and non-alphanumeric characters from the input string.
"""

import re

def clean_string(input_string):
    """
    This function removes all whitespace characters and non-alphanumeric characters from the input string.
    
    Args:
        input_string (str): The input string to be cleaned.
    
    Returns:
        str: The cleaned string with no whitespace and non-alphanumeric characters.
    """
    cleaned_string = re.sub(r'\W+','', input_string)
    return cleaned_string