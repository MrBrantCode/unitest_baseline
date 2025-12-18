"""
QUESTION:
Create a regular expression that matches all English alphabets (both lowercase and uppercase) except for the letters 'a' and 'e'. The function name should be `match_alphabets`.
"""

import re

def match_alphabets(s):
    """
    This function checks if the input string contains only English alphabets except 'a' and 'e'.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    bool: True if the string matches the pattern, False otherwise.
    """
    pattern = "^[b-df-zB-DF-Z]+$"
    return bool(re.match(pattern, s))