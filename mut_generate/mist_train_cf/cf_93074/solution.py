"""
QUESTION:
Create a function named `power` that calculates the result of a positive integer `base` raised to a positive integer `exponent`. The function should not use the built-in power operator (`**`) and should only work for positive integer inputs greater than zero.
"""

def power(base, exponent):
    """
    Calculate the result of a positive integer `base` raised to a positive integer `exponent`.

    Args:
        base (int): The base number.
        exponent (int): The exponent.

    Returns:
        int: The result of `base` raised to the power of `exponent`.
    """
    result = 1
    for _ in range(exponent):
        result *= base
    return result