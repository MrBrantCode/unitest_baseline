"""
QUESTION:
Construct a function called `hex_to_decimal` that takes an array of hexadecimal string representations as input and returns an array of their decimal integer equivalents. Each hexadecimal string in the input array should be converted to a decimal integer and the resulting integers should be stored in the output array in the same order as their corresponding input strings.
"""

def hex_to_decimal(hex_array):
    decimal_array = [int(hex_string, 16) for hex_string in hex_array]
    return decimal_array