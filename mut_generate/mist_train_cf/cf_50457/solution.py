"""
QUESTION:
Write a function `count_uppercase` that takes a string as input and returns the total number of uppercase alphabets in the string.
"""

def count_uppercase(s):
    """
    Returns the total number of uppercase alphabets in the input string.

    Args:
        s (str): The input string.

    Returns:
        int: The total number of uppercase alphabets in the string.
    """
    return sum(1 for char in s if char.isupper())