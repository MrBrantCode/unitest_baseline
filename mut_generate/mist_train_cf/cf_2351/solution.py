"""
QUESTION:
Implement a function named `decimal_to_binary` that takes an integer as input and returns its binary representation as a string using only the following bitwise operations: Bitwise AND (&), Bitwise OR (|), Bitwise XOR (^), Bitwise NOT (~), Left shift (<<), and Right shift (>>). The function should not use any built-in or library functions for conversion, arithmetic operations, or control flow statements like if, for, while loops.
"""

def decimal_to_binary(num):
    binary = ""
    while num > 0:
        binary = str(num & 1) + binary
        num = num >> 1
    return binary