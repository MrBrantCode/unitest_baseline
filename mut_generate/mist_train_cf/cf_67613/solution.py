"""
QUESTION:
Create a function named `is_palindrome` that takes an integer as input and returns a boolean indicating whether the number is a palindrome. A palindrome is a number that reads the same forwards and backwards. The solution should be able to handle large numbers efficiently.
"""

def is_palindrome(num):
    """
    Checks if the given integer is a palindrome.

    Args:
    num (int): The input number.

    Returns:
    bool: True if the number is a palindrome, False otherwise.
    """
    return str(num) == str(num)[::-1]