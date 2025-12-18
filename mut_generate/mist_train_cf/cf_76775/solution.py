"""
QUESTION:
Create a function `match_morning_universe` that takes a string input and returns `True` if the string contains the exact lexical elements "morning" and "universe" in any order, and `False` otherwise. The function should consider "morning" and "universe" as whole words, not part of another word, and the words can be separated by any characters, including spaces and punctuation.
"""

import re

def match_morning_universe(s):
    """
    This function checks if a given string contains the exact lexical elements "morning" and "universe" in any order.
    
    Parameters:
    s (str): The input string to be checked.
    
    Returns:
    bool: True if the string contains both "morning" and "universe" as whole words, False otherwise.
    """
    pattern = r".*\bmorning\b.*\buniverse\b.*|.*\buniverse\b.*\bmorning\b.*"
    return bool(re.match(pattern, s, re.DOTALL))