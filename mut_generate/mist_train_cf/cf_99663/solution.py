"""
QUESTION:
Write a function `is_divisible_by_six` that takes an integer `n` as input and returns a boolean indicating whether `n` is divisible by 6. The function should use the modulo operator to check for divisibility.
"""

def is_divisible_by_six(n):
    """
    Returns a boolean indicating whether the input integer is divisible by 6.

    Args:
        n (int): The input integer to check.

    Returns:
        bool: True if the number is divisible by 6, False otherwise.
    """
    return n % 6 == 0