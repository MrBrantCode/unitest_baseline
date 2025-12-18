"""
QUESTION:
Write a function called `trailingZeroes` that takes a positive integer `n` as input and returns the number of trailing zeroes in the factorial of `n` without using division or modulo operations.
"""

def trailingZeroes(n: int) -> int:
    """
    This function calculates the number of trailing zeroes in the factorial of a given number.

    Args:
        n (int): A positive integer.

    Returns:
        int: The number of trailing zeroes in the factorial of n.
    """
    count = 0
    i = 5
    while n // i >= 1:
        count += n // i
        i *= 5
    return count