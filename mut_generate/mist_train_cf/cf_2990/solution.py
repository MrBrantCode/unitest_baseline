"""
QUESTION:
Create a function `extract_names` that uses regular expression to extract names from a given string. The names should be in the format "First Last" and only include alphabetical characters. The function should not extract any middle initials that might be present in the names.
"""

import re

def extract_names(s):
    """
    Extracts names from a given string. The names should be in the format "First Last" 
    and only include alphabetical characters. The function does not extract any middle 
    initials that might be present in the names.

    Args:
        s (str): The input string containing names.

    Returns:
        list: A list of names extracted from the input string.
    """
    pattern = r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b'
    return re.findall(pattern, s)