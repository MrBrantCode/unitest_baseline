"""
QUESTION:
Write a function named `decimal_to_binary` that takes an integer as input and returns its binary representation as an integer using only bitwise operators. The function should not use any built-in functions for converting decimal to binary, division, or string manipulation. The input integer will be a non-negative number.
"""

def decimal_to_binary(n):
    """
    This function takes an integer as input and returns its binary representation as an integer using only bitwise operators.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The binary representation of the input integer as an integer.
    """
    binary = 0
    power = 1

    while n > 0:
        remainder = n & 1  # Get the remainder by performing a bitwise AND with 1
        binary += remainder * power  # Add the remainder to the binary representation
        n >>= 1  # Shift the decimal number right by 1
        power <<= 1  # Shift the power left by 1

    return binary