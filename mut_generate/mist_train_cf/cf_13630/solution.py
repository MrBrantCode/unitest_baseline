"""
QUESTION:
Write a function named `binary_to_int` that takes a string of binary digits (0s and 1s) as input and returns its equivalent integer value without using any built-in functions or libraries. The input string can be any length and only contains binary digits. The function should handle this conversion without relying on built-in functions for conversion.
"""

def binary_to_int(binary_num):
    """
    Convert a binary string to its equivalent integer value.

    Args:
    binary_num (str): A string of binary digits (0s and 1s).

    Returns:
    int: The integer value equivalent to the binary string.

    """
    result = 0
    for bit in binary_num:
        result = result * 2 + (ord(bit) - ord('0'))
    return result