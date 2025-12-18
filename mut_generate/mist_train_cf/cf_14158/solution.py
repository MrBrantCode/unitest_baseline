"""
QUESTION:
Write a function `hex_to_decimal` that takes a string representing a hexadecimal number as input and returns its corresponding decimal representation. The input string should be interpreted as a base-16 number.
"""

def hex_to_decimal(hex_num):
    """
    Converts a hexadecimal number to its decimal representation.

    Args:
        hex_num (str): A string representing a hexadecimal number.

    Returns:
        int: The decimal representation of the input hexadecimal number.
    """
    decimal_num = int(hex_num, 16)
    return decimal_num