"""
QUESTION:
Complete the function which converts hex number (given as a string) to a decimal number.
"""

def hex_to_decimal(hex_string: str) -> int:
    """
    Converts a hexadecimal number (given as a string) to a decimal number.

    Parameters:
    hex_string (str): The hexadecimal number to be converted.

    Returns:
    int: The decimal equivalent of the input hexadecimal number.
    """
    return int(hex_string, 16)