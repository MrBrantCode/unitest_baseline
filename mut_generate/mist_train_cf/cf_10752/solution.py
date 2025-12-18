"""
QUESTION:
Write a function `remove_special_chars` that takes a string as input, removes all special characters and numbers except for '#' and '@', and returns the resulting string. The function should preserve all alphabetic characters and whitespace.
"""

import re

def remove_special_chars(input_string):
    """
    Removes all special characters and numbers from the input string, except for '#' and '@'.
    Preserves all alphabetic characters and whitespace.

    Args:
        input_string (str): The input string to process.

    Returns:
        str: The resulting string after removing special characters and numbers.
    """
    pattern = r'[^#@a-zA-Z\s]'
    return re.sub(pattern, '', input_string)