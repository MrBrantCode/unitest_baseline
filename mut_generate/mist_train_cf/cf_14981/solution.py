"""
QUESTION:
Write a function `hex_to_binary` that takes a hexadecimal number as input and returns its binary representation as a string using only bitwise operations. The function should handle hexadecimal numbers of any length.
"""

def hex_to_binary(hex_string):
    return bin(int(hex_string, 16))[2:]