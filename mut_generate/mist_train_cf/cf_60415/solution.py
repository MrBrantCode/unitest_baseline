"""
QUESTION:
Write a function `multiply_digits(n)` that takes an integer `n` as input and returns the product of its individual digits. The function should work for any non-negative integer.
"""

def multiply_digits(n):
    """
    This function calculates the product of individual digits of a given non-negative integer.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The product of the individual digits of n.
    """
    product = 1
    while n > 0:
        digit = n % 10
        product *= digit
        n = n // 10
    return product