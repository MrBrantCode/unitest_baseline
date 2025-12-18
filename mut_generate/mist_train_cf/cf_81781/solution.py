"""
QUESTION:
Create a function `segregate_alphanumeric` that takes a string `paragraph` as input and returns two lists: one containing all alphanumeric characters and the other containing all non-alphanumeric characters. The function should use the `re` module and regular expressions to identify alphanumeric characters. The function should consider alphanumeric characters as letters, numbers, and underscores, and non-alphanumeric characters as all other characters including spaces and punctuation marks.
"""

import re

def segregate_alphanumeric(paragraph):
    """
    This function takes a string paragraph as input and returns two lists:
    one containing all alphanumeric characters and the other containing all non-alphanumeric characters.
    
    Parameters:
    paragraph (str): The input string.
    
    Returns:
    tuple: A tuple of two lists. The first list contains alphanumeric characters,
           and the second list contains non-alphanumeric characters.
    """
    alphanumeric = re.findall(r'\w', paragraph)
    non_alphanumeric = re.findall(r'\W', paragraph)
    return alphanumeric, non_alphanumeric