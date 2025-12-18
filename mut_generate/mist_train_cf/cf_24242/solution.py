"""
QUESTION:
Create a function `extract_first_name` that takes a full name string as input and returns the first name. The input string may contain additional information beyond the full name. The first name can be followed by any number of names (middle names) separated by spaces, and then any other characters. The function should only use regular expressions to extract the first name.
"""

import re

def extract_first_name(full_name):
    """
    Extract the first name from a full name string.
    
    Args:
    full_name (str): The full name string.
    
    Returns:
    str: The first name.
    """
    match = re.match(r'^\b([A-Za-z]+)', full_name)
    return match.group(0) if match else ''