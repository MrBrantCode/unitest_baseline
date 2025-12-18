"""
QUESTION:
Extract all words in a string that are surrounded by spaces, excluding the first and last word if they are not enclosed by spaces.

Function name: The solution should utilize the `re.findall()` method in Python. 

Restrictions: The solution should not include the first word if it is not preceded by a space, and it should not include the last word if it is not followed by a space.
"""

import re

def extract_enclosed_words(input_string):
    """
    Extract all words in a string that are surrounded by spaces.
    
    Args:
    input_string (str): The input string from which words will be extracted.
    
    Returns:
    list: A list of words that are enclosed by spaces.
    """
    return re.findall(r'(?<= ).*?(?= )', input_string)