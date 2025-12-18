"""
QUESTION:
Create a function called `hex_to_bin` that takes a hexadecimal string as input and returns its binary representation as a string. The hexadecimal string does not have the '0x' prefix.
"""

def hex_to_bin(hexadecimal_str):
    return bin(int(hexadecimal_str, 16))[2:]