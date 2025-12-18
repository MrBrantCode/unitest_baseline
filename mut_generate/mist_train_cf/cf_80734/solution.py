"""
QUESTION:
Develop a function `int_to_bin` that converts an integer into its binary representation. The function should handle both positive and negative integers. For negative integers, it should return the 2's complement binary form. The function should not use any built-in binary conversion functions. However, in this case, using the built-in `bin` function is acceptable due to the complexity of manual conversion. The binary representation should be 32-bit.
"""

def int_to_bin(n):
    if n < 0:
        # if the number is negative, add 2^32 to it and then convert to binary
        bin_str = bin(n + 2**32)[2:]
    else:
        bin_str = bin(n)[2:]
    return bin_str