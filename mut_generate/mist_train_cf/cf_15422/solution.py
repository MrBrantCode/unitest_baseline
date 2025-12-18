"""
QUESTION:
Write a function `decimal_to_binary` that takes an integer as input and returns its binary representation as an integer using only bitwise operations. You cannot use the bitwise shift operators (`<<` and `>>`) or the bitwise not operator (`~`).
"""

def decimal_to_binary(n):
    """
    Converts a decimal number to binary using bitwise operations.

    Args:
    n (int): The decimal number to be converted.

    Returns:
    int: The binary representation of the decimal number.
    """
    binary = 0
    power = 1
    while n != 0:
        binary += (n & 1) * power
        n = n // 2
        power *= 10
    return binary