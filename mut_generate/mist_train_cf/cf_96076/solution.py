"""
QUESTION:
Write a function `convert` that takes an integer as input and returns its binary string representation. If the input is a negative number, return its two's complement binary string representation, using 8-bit two's complement.
"""

def convert(decimal_number):
    # Handling negative numbers
    if decimal_number < 0:
        binary_representation = bin(decimal_number & 0xFF)[2:]  # Use 8-bit two's complement representation
    else:
        binary_representation = bin(decimal_number)[2:]

    return binary_representation