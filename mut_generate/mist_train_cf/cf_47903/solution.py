"""
QUESTION:
Create a function `identify_lamb_string` that takes a string `text` as input and returns `True` if the string contains the words "Mary", "had", "a", "little", and "lamb" in any order, and `False` otherwise. The function should ignore the order of words, the amount of words between them, and any variations in the words (e.g., "has" instead of "had", "Mary's" instead of "Mary").
"""

import re

def identify_lamb_string(text):
    """
    Checks if a given string contains the words "Mary", "had", "a", "little", and "lamb" in any order.
    
    Parameters:
    text (str): The input string to check.
    
    Returns:
    bool: True if the string contains all the words, False otherwise.
    """
    pattern = r'^(?=.*\bMary\b)(?=.*\bhad\b)(?=.*\ba\b)(?=.*\blittle\b)(?=.*\blamb\b).*'
    return bool(re.search(pattern, text, re.IGNORECASE))

# Add re.IGNORECASE to make the function case-insensitive