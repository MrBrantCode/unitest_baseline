"""
QUESTION:
Create a function `clean_string` that takes a string as input. The function should remove leading and trailing whitespace from the input string, convert it to lowercase, and remove all punctuation marks and non-alphanumeric characters. The resulting string should contain only alphanumeric characters.
"""

import re

def clean_string(input_string):
    """
    This function cleans a given string by removing leading/trailing whitespaces, 
    converting it to lowercase, and removing all punctuation marks and non-alphanumeric characters.

    Args:
    input_string (str): The input string to be cleaned.

    Returns:
    str: The cleaned string containing only alphanumeric characters.
    """
    # Trim whitespace
    cleaned_string = input_string.strip()

    # Convert to lowercase
    cleaned_string = cleaned_string.lower()

    # Remove punctuation marks and non-alphanumeric characters
    cleaned_string = re.sub(r"[^\w\s]", "", cleaned_string)

    return cleaned_string