"""
QUESTION:
Write a function named `is_anagram` that takes a string as input and returns `True` if the input string is the same when its characters are reversed, and `False` otherwise. The function should not take any other inputs besides the string.
"""

def is_anagram(word):
    """
    Returns True if the input string is the same when its characters are reversed, False otherwise.

    Args:
        word (str): The input string to check.

    Returns:
        bool: Whether the input string is the same when reversed.
    """
    return word == word[::-1]