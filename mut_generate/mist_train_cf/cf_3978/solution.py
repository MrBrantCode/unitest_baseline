"""
QUESTION:
Create a regular expression that matches strings containing zero or more non-digit characters. The string should not end with a digit.
"""

import re

def entrance(s):
    """
    Checks if a string contains zero or more non-digit characters and does not end with a digit.
    
    Parameters:
    s (str): The input string to be checked.
    
    Returns:
    bool: True if the string matches the condition, False otherwise.
    """
    return bool(re.match(r'^\D*$', s))