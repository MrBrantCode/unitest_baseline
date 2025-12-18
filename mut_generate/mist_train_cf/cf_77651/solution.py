"""
QUESTION:
Create a function `remove_non_alphanumeric_characters(s)` that takes a string `s` containing UTF-8 encoded characters as input and returns the string with all non-alphanumeric characters removed. The function should exclude spaces from the removal by default, but provide an alternative solution that includes spaces in the removal if required.
"""

import re

def remove_non_alphanumeric_characters(s):
    """
    Removes all non-alphanumeric characters from a given string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    str: The string with all non-alphanumeric characters removed.
    """
    # By default, this function excludes spaces from removal
    return re.sub(r'[^a-zA-Z0-9 ]', '', s)

# Alternative solution that includes spaces in the removal
def remove_non_alphanumeric_characters_including_spaces(s):
    """
    Removes all non-alphanumeric characters and spaces from a given string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    str: The string with all non-alphanumeric characters and spaces removed.
    """
    return re.sub(r'\W+', '', s)