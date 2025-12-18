"""
QUESTION:
Write a function `add_without_conversion(a, b)` that takes two integers `a` and `b` as input and returns their sum without any type conversion, using only bitwise operators. The function should not use any arithmetic operators for addition.
"""

def add_without_conversion(a, b):
    """
    This function adds two integers without any type conversion using only bitwise operators.

    Args:
        a (int): The first integer to be added.
        b (int): The second integer to be added.

    Returns:
        int: The sum of the two integers.
    """
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a