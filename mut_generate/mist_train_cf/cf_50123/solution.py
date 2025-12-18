"""
QUESTION:
Create a function `check_string` that takes a string as input and returns True if the string contains "hello" or "world" and either starts with a number or ends with an uppercase letter, otherwise returns False.
"""

import re

def check_string(s):
    """
    Checks if the input string contains "hello" or "world" and either starts with a number or ends with an uppercase letter.

    Args:
    s (str): The input string.

    Returns:
    bool: True if the string meets the conditions, False otherwise.
    """
    pattern = r'(^[0-9].*(hello|world))|((hello|world).*[A-Z]$)'
    return bool(re.search(pattern, s, re.IGNORECASE))