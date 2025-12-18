"""
QUESTION:
Write a function `is_palindrome` that takes a string as input and returns a boolean indicating whether the string is a palindrome. The input string will be a single word without spaces or punctuation.
"""

def is_palindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome.

    Args:
    s (str): The input string.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    return s == s[::-1]