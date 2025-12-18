"""
QUESTION:
Write a Python function `hex_to_bin` that takes a string representing a hexadecimal number and returns its binary representation as a string. The binary string should not include the '0b' prefix and should be padded with leading zeros to a length equal to 4 times the length of the input string.
"""

def hex_to_bin(hex_value):
    scale = 16 
    num_of_bits = 4
    return bin(int(hex_value, scale))[2:].zfill(len(hex_value)*num_of_bits)