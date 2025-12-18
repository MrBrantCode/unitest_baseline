"""
QUESTION:
Write a function `decimal_to_binary(num)` that takes an integer `num` as input and returns its binary representation as a string, without using any built-in or library functions for conversion. The function should only use the following bitwise operations: `&`, `|`, `^`, `~`, `<<`, and `>>`.
"""

def decimal_to_binary(num):
    binary = ""
    while num > 0:
        binary = str(num & 1) + binary
        num >>= 1
    return binary