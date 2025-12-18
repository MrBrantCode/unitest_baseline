"""
QUESTION:
Create a function called `hex_to_binary` that takes a hexadecimal string as input and returns its corresponding binary representation. The binary representation should be a string of binary digits without the '0b' prefix. The function should be able to handle hexadecimal strings of varying lengths.
"""

def hex_to_binary(hex_string):
    return bin(int(hex_string, 16))[2:]