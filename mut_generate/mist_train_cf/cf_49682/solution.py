"""
QUESTION:
Create a function named `hex_to_bin` that takes a hexadecimal string as input and returns its binary equivalent as a string. The input hexadecimal string should be converted to decimal first, then to binary, and the output binary string should not include the "0b" prefix.
"""

def hex_to_bin(hex_val):
    bin_val = bin(int(hex_val, 16))[2:]
    return bin_val