"""
QUESTION:
Implement a Calculator interface with an add, subtract, and multiply method. The multiply method should multiply two integers using bitwise operations only, handle negative numbers correctly, and have a time complexity of O(log n), where n is the larger of the two input numbers. The method should take two integers as parameters and return the product of the two numbers.
"""

def multiply(a, b):
    """
    Multiply two integers using bitwise operations.

    Args:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The product of the two integers.
    """
    is_negative = (a < 0) ^ (b < 0)
    a = abs(a)
    b = abs(b)

    result = 0
    while b > 0:
        if b & 1:
            result += a
        a <<= 1
        b >>= 1

    return -result if is_negative else result