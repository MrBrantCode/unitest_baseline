"""
QUESTION:
Create a function called `remove_punctuation` that takes a string as input and returns a string with all punctuation removed. The function should utilize Python's built-in `re` module for regular expression operations.
"""

import re

def remove_punctuation(text):
    """
    This function takes a string as input, removes all punctuation, 
    and returns the resulting string.
    
    Parameters:
    text (str): The input string from which punctuation is to be removed.
    
    Returns:
    str: The input string with all punctuation removed.
    """
    pattern = r'[^\w\s]'
    text_no_punctuation = re.sub(pattern, "", text)
    return text_no_punctuation