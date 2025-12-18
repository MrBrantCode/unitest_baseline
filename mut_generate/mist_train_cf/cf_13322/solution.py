"""
QUESTION:
Write a function `count_ab` that takes a string as input and returns the number of occurrences of the letter "a" (either uppercase or lowercase) immediately followed by the letter "b" (either uppercase or lowercase).
"""

def count_ab(s):
    """
    Returns the number of occurrences of the letter "a" (either uppercase or lowercase) 
    immediately followed by the letter "b" (either uppercase or lowercase) in the given string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of occurrences of "ab" or "AB" in the string.
    """
    return s.lower().count("ab")