"""
QUESTION:
Write a function `hex_to_bin` that takes a hexadecimal number as a string and returns its binary representation as a string. The function should be able to handle any valid hexadecimal input.
"""

def hex_to_bin(hex_num):
    bin_num = bin(int(hex_num, 16))[2:]
    return bin_num