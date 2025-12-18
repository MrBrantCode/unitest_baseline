"""
QUESTION:
Extract the integer value enclosed within parentheses from a given string using the function `extract_integer_value`. The integer value will always be followed by the word "value" and will be enclosed within parentheses. The function should return the extracted integer value if found, otherwise return a message indicating that no integer value was found.
"""

import re

def extract_integer_value(s):
    """
    Extract the integer value enclosed within parentheses from a given string.
    
    Args:
    s (str): The input string containing the integer value.
    
    Returns:
    int or str: The extracted integer value if found, otherwise a message indicating that no integer value was found.
    """
    match = re.search(r'\((\d+)\) value', s)
    
    if match:
        return int(match.group(1))
    else:
        return "No integer value found."