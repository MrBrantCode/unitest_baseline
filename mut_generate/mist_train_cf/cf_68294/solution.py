"""
QUESTION:
Write a function named `hex_to_bin` that takes a string of hexadecimal digits as input and returns the corresponding binary number as a string. The hexadecimal input should be converted to decimal and then to binary, with the '0b' prefix removed from the binary output.
"""

def hex_to_bin(hex_number):
    """
    Converts a hexadecimal number to a binary number.
    
    Parameters:
    hex_number (str): A string of hexadecimal digits.
    
    Returns:
    str: The corresponding binary number as a string.
    """
    bin_number = bin(int(hex_number, 16))
    return bin_number[2:]