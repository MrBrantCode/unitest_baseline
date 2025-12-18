"""
QUESTION:
Write a function `split_string(string)` that splits a given string into a list of substrings using any special characters or digits present in the string as delimiters. The function should include the substrings between the delimiters, as well as the delimiters themselves, in the resulting list. Consecutive delimiters and empty substrings should be handled appropriately. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.
"""

import re

def split_string(string):
    """
    Splits a given string into a list of substrings using any special characters or digits present in the string as delimiters.
    
    Args:
        string (str): The input string to be split.
    
    Returns:
        list: A list of substrings and delimiters.
    """
    substrings = re.split(r'(\W+|\d+)', string)
    return [substring for substring in substrings if substring != '']