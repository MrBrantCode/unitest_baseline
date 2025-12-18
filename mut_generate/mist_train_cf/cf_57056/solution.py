"""
QUESTION:
Write a function named hexadecimal_to_binary that converts a given hexadecimal number into its equivalent binary value. The input is a string representing the hexadecimal number. The function should return a string representing the binary number. The binary string should not include the '0b' prefix.
"""

def hexadecimal_to_binary(hex_string):
    return bin(int(hex_string, 16))[2:]