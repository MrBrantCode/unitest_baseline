"""
QUESTION:
Write a function `hex_to_bin(hex_num)` that takes a string `hex_num` representing a hexadecimal number (including 'a-f' values) and returns its binary representation as a string. The function should be able to handle large hexadecimal numbers.
"""

def hex_to_bin(hex_num):
    bin_num = bin(int(hex_num, 16))[2:]
    return bin_num