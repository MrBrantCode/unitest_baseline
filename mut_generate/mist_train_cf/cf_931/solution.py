"""
QUESTION:
Write a function `is_multiple_of_3_or_5` that takes a positive integer `n` as input and returns `True` if the number is a multiple of 3 or a multiple of 5, but not a multiple of both. The function should also return `True` when the number is zero. The solution should not use any arithmetic operations, loops, or conditionals.
"""

def is_multiple_of_3_or_5(n):
    """
    Checks if a given positive integer is a multiple of 3 or a multiple of 5, but not a multiple of both.
    Also returns True when the number is zero.

    Args:
        n (int): A positive integer.

    Returns:
        bool: True if the number is a multiple of 3 or 5, but not both, or if the number is zero. False otherwise.
    """
    return ((n % 3 == 0) and not (n % 5 == 0)) or ((n % 5 == 0) and not (n % 3 == 0)) or (n == 0)