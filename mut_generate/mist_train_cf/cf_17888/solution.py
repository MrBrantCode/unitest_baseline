"""
QUESTION:
Write a function `extract_unique_chars` that takes a string of alphabetic characters as input, where the length of the string is between 10 and 100 characters (inclusive). The function should return a list of unique characters in the string, sorted in alphabetical order.
"""

def extract_unique_chars(s):
    """
    Returns a list of unique characters in the input string, sorted in alphabetical order.

    Args:
        s (str): The input string of alphabetic characters.

    Returns:
        list: A list of unique characters in the string, sorted in alphabetical order.
    """
    return sorted(list(set(char for char in s)))