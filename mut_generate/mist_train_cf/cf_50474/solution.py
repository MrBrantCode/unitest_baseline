"""
QUESTION:
Write a function called `hex_to_decimal` that converts a given hexadecimal number to its decimal representation. The input will be a string representing a hexadecimal number (prefix '0x' or '0X' is optional). The function should return the decimal equivalent of the input hexadecimal number.
"""

def hex_to_decimal(hex_value):
    """
    Converts a given hexadecimal number to its decimal representation.

    Args:
        hex_value (str): A string representing a hexadecimal number.
                         The prefix '0x' or '0X' is optional.

    Returns:
        int: The decimal equivalent of the input hexadecimal number.
    """
    return int(hex_value, 16)