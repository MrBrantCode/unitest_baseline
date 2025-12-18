"""
QUESTION:
Write a function named 'find_semicolons' that uses a regular expression to find all occurrences of ';' in a given string and returns a list of matches.
"""

import re

def find_semicolons(s):
    """
    This function finds all occurrences of ';' in a given string.
    
    Parameters:
    s (str): The string to search for semicolons.
    
    Returns:
    list: A list of matches.
    """
    return re.findall(';', s)