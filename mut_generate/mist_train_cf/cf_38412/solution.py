"""
QUESTION:
Given an integer `n`, write a function `reverseBits` that reverses the bits of `n` and returns the resulting integer. The input `n` is a 32-bit signed integer.
"""

def reverseBits(n):
    """
    Reverses the bits of a given 32-bit signed integer.

    Args:
        n (int): A 32-bit signed integer.

    Returns:
        int: The integer with its bits reversed.
    """
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result