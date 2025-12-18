"""
QUESTION:
Create a regular expression to match a string of consecutive numbers with a minimum of 4 digits that is enclosed within double quotes. The string should not contain any whitespace characters. The regular expression should match the entire string, from start to end, and ensure that the double quotes are part of the match.
"""

import re

def match_consecutive_numbers(s):
    """
    This function checks if a given string matches the pattern of a string of consecutive numbers 
    with a minimum of 4 digits enclosed within double quotes.
    
    Parameters:
    s (str): The input string to be checked.
    
    Returns:
    bool: True if the string matches the pattern, False otherwise.
    """
    pattern = r'^"\d{4,}"$'
    return bool(re.match(pattern, s))