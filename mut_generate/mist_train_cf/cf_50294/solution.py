"""
QUESTION:
Write a function named `reversed_bits_decimal` that takes an integer `n` as input and returns the decimal representation of the reversed binary bits of `n`. The function should not use any built-in functions to reverse the binary string. However, the use of the built-in `bin()` and `int()` functions for decimal to binary and binary to decimal conversions respectively is allowed. The input `n` is a non-negative integer.
"""

def reversed_bits_decimal(n):
    binary_repr = bin(n).replace("0b", "")
    reversed_binary_repr = binary_repr[::-1]
    reversed_decimal = int(reversed_binary_repr, 2)
    
    return reversed_decimal