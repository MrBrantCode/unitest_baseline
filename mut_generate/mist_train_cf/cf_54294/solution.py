"""
QUESTION:
Create a function `is_valid_ip` that takes a string as input and returns `True` if the string contains a valid IP address, and `False` otherwise. A valid IP address is in the format of four numbers separated by periods, where each number is between 0 and 255.
"""

import re

def is_valid_ip(s):
    """
    Checks if a string contains a valid IP address.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string contains a valid IP address, False otherwise.
    """
    pattern = r"\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\b"
    return bool(re.search(pattern, s))