"""
QUESTION:
Write a function `hex_to_bin` that takes a hexadecimal string as input and returns its corresponding binary representation as a string. The input hexadecimal string may contain letters 'A-F' or 'a-f' to represent numbers 10-15. The output binary string should not have the '0b' prefix.
"""

def hex_to_bin(hexadecimal):
    binary = bin(int(hexadecimal, 16))[2:]
    return binary