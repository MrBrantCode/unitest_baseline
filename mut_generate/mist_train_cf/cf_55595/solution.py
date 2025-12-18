"""
QUESTION:
Create a function `decimal_to_binary(n)` that takes an integer `n` as input and returns its binary equivalent as a string, excluding the '0b' prefix.
"""

def decimal_to_binary(n):
    return bin(n)[2:]