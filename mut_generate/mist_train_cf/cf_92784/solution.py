"""
QUESTION:
Write a function `reverse_string` that takes a string as input and returns the reversed string without using any loops or recursion.
"""

def reverse_string(s: str) -> str:
    """
    Reverses a given string without using any loops or recursion.

    Args:
    s (str): The input string to be reversed.

    Returns:
    str: The reversed string.
    """
    return s[::-1]