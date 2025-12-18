"""
QUESTION:
Write a function `binary_to_hex` that takes a binary number as a string and returns its hexadecimal representation as a string. The function should not include the '0x' prefix in the output. The binary number is guaranteed to be a string of '0's and '1's.
"""

def binary_to_hex(binary):
    return hex(int(binary, 2))[2:]