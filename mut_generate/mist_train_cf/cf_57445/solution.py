"""
QUESTION:
Create a function `clean_string` that takes an input string, removes special characters and digits, and replaces consecutive whitespaces with a single whitespace. The function should return the cleaned string.
"""

import re

def clean_string(input_string):
    """
    This function takes an input string, removes special characters and digits, 
    and replaces consecutive whitespaces with a single whitespace.

    Args:
    input_string (str): The string to be cleaned.

    Returns:
    str: The cleaned string.
    """
    # Remove special characters and digits
    cleaned_string = re.sub('[^A-Za-z\s]', '', input_string)

    # Replace multiple whitespaces with a single whitespace
    cleaned_string = re.sub('\s+', ' ', cleaned_string)

    return cleaned_string.strip()  # Remove leading/trailing whitespaces