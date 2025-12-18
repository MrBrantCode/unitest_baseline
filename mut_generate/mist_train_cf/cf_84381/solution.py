"""
QUESTION:
Create a function `hex_to_bin(hex_string)` that converts a given hexadecimal string into a binary string, ensuring that each hexadecimal digit corresponds to exactly 4 binary digits by padding with leading zeros if necessary. The input hexadecimal string is expected to be a valid hexadecimal number without the '0x' prefix.
"""

def hex_to_bin(hex_string):
    bin_string = bin(int(hex_string, 16))[2:]
    return bin_string.zfill(4 * len(hex_string))