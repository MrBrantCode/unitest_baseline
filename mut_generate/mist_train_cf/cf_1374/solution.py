"""
QUESTION:
Implement a function `decimal_to_hexadecimal(n)` that takes a positive integer `n` as input and returns its hexadecimal representation using bitwise operations. The function should have a time complexity of O(log n) and be implemented using a recursive algorithm.
"""

def decimal_to_hexadecimal(n):
    """
    Converts a positive integer to its hexadecimal representation using bitwise operations.

    Args:
        n (int): A positive integer.

    Returns:
        str: The hexadecimal representation of n.
    """
    hex_chars = "0123456789ABCDEF"
    if n < 16:
        return hex_chars[n]
    else:
        return decimal_to_hexadecimal(n >> 4) + hex_chars[n & 15]