"""
QUESTION:
Write a regex pattern to match all words in a string that start with a lowercase letter, have at least one uppercase letter in the middle, and end with an uppercase letter. The words should only contain letters, with no special characters or numbers in between.
"""

import re

def entrance(string):
    """
    Returns all words in the given string that start with a lowercase letter, 
    have at least one uppercase letter in the middle, and end with an uppercase letter.
    
    Parameters:
    string (str): The input string to search for words.
    
    Returns:
    list: A list of words that match the specified pattern.
    """
    pattern = r'\b[a-z][a-zA-Z]*[A-Z]\b'
    matches = re.findall(pattern, string)
    return matches