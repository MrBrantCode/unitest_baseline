"""
QUESTION:
Write a function called `regex_match` that takes a pattern and a string as input and returns all matches of the pattern in the string, considering the complexities of matching nested patterns and quantifiers, and utilizing lookaheads and lookbehinds. The function should return all matches in a list, regardless of case.
"""

import re

def regex_match(pattern, string):
    """
    This function takes a pattern and a string as input and returns all matches of the pattern in the string.
    
    Args:
        pattern (str): The regular expression pattern to be matched.
        string (str): The string in which the pattern will be searched.
    
    Returns:
        list: A list of all matches of the pattern in the string, regardless of case.
    """
    return re.findall(pattern, string, re.I)