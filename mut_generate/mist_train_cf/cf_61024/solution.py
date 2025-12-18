"""
QUESTION:
Create a function named `hex_to_bin` that takes a string `hex_num` representing a hexadecimal number as input and returns its binary representation as a string. The input string will only contain hexadecimal digits (0-9, A-F). The output string should not include the '0b' prefix.
"""

def hex_to_bin(hex_num):
    return bin(int(hex_num, 16))[2:]