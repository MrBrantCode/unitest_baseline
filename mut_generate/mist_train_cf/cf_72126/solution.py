"""
QUESTION:
Create a function called `hex_to_bin` that converts a hexadecimal number to a binary number. The function should handle negative hexadecimal numbers and return the binary representation as a string. The input hexadecimal number is represented as a string, and the function should return a string starting with '-' if the input is negative.
"""

def hex_to_bin(hex_number):
    # Check if the hex_number is negative
    if hex_number[0] == '-':
        return "-" + bin(int(hex_number[1:], 16))[2:]
    else:
        return bin(int(hex_number, 16))[2:]