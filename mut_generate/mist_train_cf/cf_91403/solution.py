"""
QUESTION:
Implement a function `decimal_to_binary(num)` that takes an integer as input and returns its binary representation as a string without using any built-in or library functions for conversion. The function should handle 32-bit integers.
"""

def decimal_to_binary(num):
    binary = ""
    for i in range(31, -1, -1):
        shifted_value = num >> i
        if shifted_value & 1:
            binary += '1'
        else:
            binary += '0'
    return binary