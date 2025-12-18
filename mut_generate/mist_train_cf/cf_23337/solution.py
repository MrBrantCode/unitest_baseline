"""
QUESTION:
Create a function `power(base, exp)` that calculates the value of `base` raised to the power of `exp` using an iterative approach. The function should return an integer result. The `base` and `exp` will be integers, and `exp` is non-negative.
"""

def power(base, exp):
    """
    Calculate the value of `base` raised to the power of `exp` using an iterative approach.

    Args:
        base (int): The base number.
        exp (int): The exponent, a non-negative integer.

    Returns:
        int: The result of `base` raised to the power of `exp`.
    """
    result = 1
    while exp != 0:
        result *= base
        exp -= 1
    return result