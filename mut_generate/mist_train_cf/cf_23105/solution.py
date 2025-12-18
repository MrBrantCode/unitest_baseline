"""
QUESTION:
Write a function named hex_to_binary that takes a hexadecimal string as input and returns its binary representation as a string. The function should only use bitwise operations to perform the conversion.
"""

def hex_to_binary(hex_string):
    """
    This function takes a hexadecimal string as input and returns its binary representation as a string.
    It uses bitwise operations to perform the conversion.

    Parameters:
    hex_string (str): A string of hexadecimal digits.

    Returns:
    str: The binary representation of the input hexadecimal string.
    """
    # Convert the hexadecimal string to an integer
    decimal_value = int(hex_string, 16)
    
    # Convert the decimal integer to binary and remove the '0b' prefix
    binary_value = bin(decimal_value)[2:]
    
    # Return the binary representation
    return binary_value