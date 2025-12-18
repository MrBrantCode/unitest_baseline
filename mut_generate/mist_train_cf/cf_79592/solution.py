"""
QUESTION:
Write a function `hex_to_binary(x: str)` that takes a hexadecimal string `x` as input and returns its corresponding binary representation as a string. The function should not include the '0b' prefix in the binary output. The input string `x` is a valid hexadecimal number.
"""

def hex_to_binary(x: str):
    return bin(int(x, 16))[2:]