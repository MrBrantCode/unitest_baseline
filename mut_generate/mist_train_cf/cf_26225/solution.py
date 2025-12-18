"""
QUESTION:
Write a function named `extract_chars` that takes a string as input and returns the first and last occurring characters from the string. The function should be able to handle strings of any length.
"""

def extract_chars(s):
    """
    Returns the first and last occurring characters from the input string.

    Args:
        s (str): The input string.

    Returns:
        tuple: A tuple containing the first and last characters of the string.
    """
    return s[0], s[-1]