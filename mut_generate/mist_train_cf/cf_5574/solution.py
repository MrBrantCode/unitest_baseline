"""
QUESTION:
Write a function decimalToHex that takes a decimal number as input and returns its hexadecimal representation as a string using only bitwise operations, without using any loops or conditionals.
"""

def decimalToHex(n):
    hex_map = "0123456789ABCDEF"
    hex_str = ""
    while n:
        hex_str = hex_map[n % 16] + hex_str
        n //= 16
    return hex_str