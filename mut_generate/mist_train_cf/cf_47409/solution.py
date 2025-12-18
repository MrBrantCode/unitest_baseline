"""
QUESTION:
Write a function `is_palindrome(num)` that checks if a given number is a palindrome. The function should return `True` if the number is the same forwards and backwards, and `False` otherwise. The input number will be a positive integer and the function should not take any other parameters.
"""

def is_palindrome(num):
    """
    Checks if a given number is a palindrome.

    Args:
        num (int): A positive integer.

    Returns:
        bool: True if the number is the same forwards and backwards, False otherwise.
    """
    return str(num) == str(num)[::-1]