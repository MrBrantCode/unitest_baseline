"""
QUESTION:
Create a function `check_string_case` that takes a string as input and returns `True` if the string contains at least one uppercase letter and one lowercase letter, and `False` otherwise. The function should use regular expressions to achieve this.
"""

import re

def check_string_case(s):
    """
    This function checks if a given string contains at least one uppercase letter and one lowercase letter.
    
    Args:
        s (str): The input string.
    
    Returns:
        bool: True if the string contains at least one uppercase letter and one lowercase letter, False otherwise.
    """
    return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z]).*$', s))