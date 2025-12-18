"""
QUESTION:
Write a function `ieee_754_representation` that takes a float number as input and returns its binary representation in IEEE 754 format as a string. The function should follow these rules: 
- The input number can be any float number.
- The output string should be in the format of 'sign bit exponent mantissa' without any spaces or separation.
- The binary representation should be for a single-precision floating-point format (32 bits).
- The exponent should be expressed as a biased representation.
- The mantissa should be normalized.
- The function should handle both positive and negative numbers.
- The function should handle rounding according to the IEEE 754 standard.
"""

import struct

def ieee_754_representation(num):
    """
    This function takes a float number as input and returns its binary representation 
    in IEEE 754 format as a string.

    Parameters:
    num (float): The float number to be converted.

    Returns:
    str: The binary representation of the float number in IEEE 754 format.
    """

    # Convert the float number to a 32-bit integer using the struct module
    int_num = struct.unpack('I', struct.pack('f', num))[0]

    # Convert the integer to a binary string and remove the '0b' prefix
    bin_num = bin(int_num)[2:].zfill(32)

    # Separate the sign bit, exponent, and mantissa
    sign_bit = bin_num[0]
    exponent = bin_num[1:9]
    mantissa = bin_num[9:]

    # Return the binary representation as a string
    return sign_bit + exponent + mantissa