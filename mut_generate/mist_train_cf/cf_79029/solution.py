"""
QUESTION:
Write a function `integer_to_binary(n)` that generates the binary representation of a given integer `n` as a string, excluding the '0b' prefix.
"""

def integer_to_binary(n):
    return bin(n)[2:]