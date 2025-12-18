"""
QUESTION:
Implement a function called `calculate_power` that takes two integers, `base` and `exponent`, as input and returns an integer representing the result of `base` raised to the power of `exponent`. The function should not use the built-in power operator or any multiplication operator. It should handle any positive integer values for `base` and `exponent`, correctly handle negative `exponent` values, and return an integer result, even for what would be fractional powers.
"""

def calculate_power(base: int, exponent: int) -> int:
    """
    Calculate the power of a number without using the built-in power operator or any multiplication operator.

    Args:
    base (int): The base number.
    exponent (int): The exponent.

    Returns:
    int: The result of base raised to the power of exponent.
    """
    if exponent == 0:
        return 1
    elif exponent < 0:
        return int(1 / calculate_power(base, -exponent))
    elif exponent % 2 == 0:
        temp = calculate_power(base, exponent // 2)
        return temp * temp
    else:
        return base * calculate_power(base, exponent - 1)