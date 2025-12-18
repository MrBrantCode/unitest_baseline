"""
QUESTION:
Write a function named `hexadecimal_representation` that takes an integer as input and returns its hexadecimal representation as a string. The function should use bitwise operations only, without any built-in conversion functions or libraries.
"""

def hexadecimal_representation(n):
    hex_map = "0123456789ABCDEF"
    hex_str = ""
    while n:
        hex_str = hex_map[n & 15] + hex_str
        n >>= 4
    return hex_str if hex_str else "0"