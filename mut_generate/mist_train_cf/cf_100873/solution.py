"""
QUESTION:
Create a function named `remove_extra_spaces` that takes a string as input, removes extra spaces and special characters (hyphens or periods) from the string, and returns the cleaned string. The function should handle inconsistent number of spaces and special characters.
"""

import re

def remove_extra_spaces(input_string):
    """
    Removes extra spaces and special characters (hyphens or periods) from the input string.

    Args:
        input_string (str): The input string to be cleaned.

    Returns:
        str: The cleaned string.
    """
    return re.sub('[\s.-]+', ' ', input_string).strip()