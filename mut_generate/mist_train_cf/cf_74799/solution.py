"""
QUESTION:
Write a function `hex_to_ascii` that takes a hexadecimal string as input and returns its equivalent ASCII character. The input hexadecimal string represents the ASCII value of a character in hexadecimal notation. The function should support hexadecimal strings of length 2.
"""

def hex_to_ascii(hex_number):
    """
    This function takes a hexadecimal string of length 2 as input and returns its equivalent ASCII character.

    Parameters:
    hex_number (str): A hexadecimal string representing the ASCII value of a character.

    Returns:
    str: The ASCII character equivalent to the input hexadecimal string.
    """
    return chr(int(hex_number, 16))