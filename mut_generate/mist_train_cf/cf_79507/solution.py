"""
QUESTION:
Create a function named `hex_to_binary` that takes a single hexadecimal digit as input and returns its binary representation as a string. The binary representation should be padded with leading zeros to a length of 4 bits.
"""

def hex_to_binary(hex_digit):
    """
    Convert a hexadecimal digit to its binary representation.

    Args:
        hex_digit (str): A single hexadecimal digit.

    Returns:
        str: The binary representation of the hexadecimal digit, padded with leading zeros to a length of 4 bits.
    """
    return bin(int(hex_digit, 16))[2:].zfill(4)