"""
QUESTION:
Implement the function `power(base, exponent)` that calculates the result of raising `base` to the power of `exponent`, where both `base` and `exponent` are whole numbers. The function should not use Python's built-in power function. The function should handle negative exponents by returning the reciprocal of the result for the corresponding positive exponent.
"""

def power(base, exponent):
    """
    Calculate the result of raising base to the power of exponent.

    Args:
    base (int): The base number.
    exponent (int): The exponent.

    Returns:
    int: The result of base raised to the power of exponent.
    """
    result = 1
    for i in range(abs(exponent)):
        result *= base
    if exponent < 0:
        return 1 / result
    else:
        return result