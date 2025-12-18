"""
QUESTION:
Write a function called `shift_right` that takes two integers as input, `n` and `k`, and returns the result of shifting the bits of `n` to the right by `k` places. The function should use the bitwise right shift operator (`>>`). The input values of `n` and `k` are non-negative integers.
"""

def shift_right(n, k):
    """
    Shift the bits of n to the right by k places.

    Args:
        n (int): The number to be shifted.
        k (int): The number of places to shift.

    Returns:
        int: The result of shifting n to the right by k places.
    """
    return n >> k