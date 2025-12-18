"""
QUESTION:
Write a function `same_chars(s0, s1)` that takes two string inputs `s0` and `s1` as arguments. The function should return `True` if both strings contain the same characters with the same counts and in the same order, ignoring case and non-alphabetic characters. Otherwise, it should return `False`.
"""

def same_chars(s0, s1):
    """
    Checks if two strings contain the same characters with the same counts and in the same order, 
    ignoring case and non-alphabetic characters.

    Args:
        s0 (str): The first input string.
        s1 (str): The second input string.

    Returns:
        bool: True if both strings contain the same characters with the same counts and in the same order, 
              False otherwise.
    """
    
    # Remove non-alphabetic characters and convert to lower case
    s0 = ''.join(filter(str.isalpha, s0)).lower()
    s1 = ''.join(filter(str.isalpha, s1)).lower()

    # Check if both strings have the same characters in the same order
    # and the same characters with the same counts
    return s0 == s1 and sorted(s0) == sorted(s1)