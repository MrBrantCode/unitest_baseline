"""
QUESTION:
Create a function `convert` that takes an integer `decimal_number` as input and returns a string representing its binary equivalent. If `decimal_number` is negative, return its 8-bit two's complement binary string representation.
"""

def convert(decimal_number):
    """
    Converts an integer to its binary string representation.
    If the number is negative, returns its 8-bit two's complement binary string representation.

    Args:
        decimal_number (int): The decimal number to convert.

    Returns:
        str: The binary string representation of the decimal number.
    """
    # Handling negative numbers
    if decimal_number < 0:
        binary_representation = bin(decimal_number & 0xFF)[2:]  # Use 8-bit two's complement representation
    else:
        binary_representation = bin(decimal_number)[2:]

    return binary_representation