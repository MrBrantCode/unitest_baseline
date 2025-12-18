"""
QUESTION:
Write a function named `decimal_to_binary(n)` that takes a decimal integer `n` in the range of 0 to 255 as input and returns its binary representation as a string using only bitwise operations.
"""

def decimal_to_binary(n):
    binary_rep = ""
    for i in range(7, -1, -1):
        bit = (n >> i) & 1
        binary_rep += str(bit)
    return binary_rep