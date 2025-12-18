"""
QUESTION:
Implement a function `binary_to_decimal` that takes a string of binary digits as input and returns its decimal equivalent without using any built-in binary to decimal conversion functions or libraries.
"""

def binary_to_decimal(binary_str):
    """
    This function converts a binary number represented as a string to its decimal equivalent.

    Args:
    binary_str (str): A string of binary digits.

    Returns:
    int: The decimal equivalent of the binary number.

    """
    decimal_num = 0
    for i, digit in enumerate(reversed(binary_str)):
        decimal_num += int(digit) * (2 ** i)
    return decimal_num