"""
QUESTION:
Write a function named `invert_num` that takes an integer `n` as input and returns the inverted integer without converting it to a string. The function should work with both positive and negative integers. The input integer `n` is a 32-bit signed integer, which means it is in the range of -2^31 to 2^31-1. The output should also be in the same range. If the inverted integer is outside this range, the function should return 0.
"""

def invert_num(n):
    """
    Inverts a 32-bit signed integer without converting it to a string.

    Args:
        n (int): A 32-bit signed integer.

    Returns:
        int: The inverted integer, or 0 if it's outside the 32-bit signed integer range.
    """
    inverted = 0
    sign = -1 if n < 0 else 1
    n *= sign

    while n:
        inverted = inverted * 10 + n % 10
        n = n // 10

    inverted *= sign

    if inverted < -2**31 or inverted > 2**31 - 1:
        return 0

    return inverted