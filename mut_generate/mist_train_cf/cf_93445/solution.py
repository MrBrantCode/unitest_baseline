"""
QUESTION:
Create a function called `trim_string` that takes a string as input, removes leading and trailing whitespace characters, and replaces any consecutive whitespace characters within the string with a single space. The function should return the resulting trimmed string.
"""

import re

def trim_string(s):
    """
    Removes leading and trailing whitespace characters from a string and replaces 
    any consecutive whitespace characters within the string with a single space.

    Args:
        s (str): The input string to be trimmed.

    Returns:
        str: The trimmed string.
    """
    return re.sub(r'\s+', ' ', s).strip()