"""
QUESTION:
Create a function `unique_chars` that takes a string of lowercase alphabetic characters as input, extracts unique characters that do not appear consecutively, and returns them in a list in alphabetical order. The input string should be between 20 and 200 characters long.
"""

def unique_chars(s):
    """
    Extracts unique characters that do not appear consecutively from a given string and returns them in a list in alphabetical order.
    
    Parameters:
    s (str): A string of lowercase alphabetic characters between 20 and 200 characters long.
    
    Returns:
    list: A list of unique characters that do not appear consecutively in alphabetical order.
    """
    return sorted(list(set(s[i] for i in range(len(s)) if i == 0 or s[i] != s[i-1])))