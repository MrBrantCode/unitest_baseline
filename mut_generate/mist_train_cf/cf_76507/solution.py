"""
QUESTION:
Write a Python function named `is_power_of_two` that takes one argument `n` and returns `True` if `n` is a power of two and `False` otherwise. The function must use bitwise operations and should not use any built-in functions or mathematical operations other than bitwise operations and comparison.
"""

def is_power_of_two(n):
    """
    This function checks if a number is a power of two using bitwise operations.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is a power of two, False otherwise.
    """
    return (n != 0) and ((n & (n - 1)) == 0)