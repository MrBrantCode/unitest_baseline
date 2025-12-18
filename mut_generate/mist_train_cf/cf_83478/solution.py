"""
QUESTION:
Write a function `hex_to_bin(hexa)` that converts a given hexadecimal number `hexa` to its binary representation. The function should handle invalid hexadecimal characters and return an error message if the input is not a valid hexadecimal number.
"""

def hex_to_bin(hexa):
    try:
        bin_num = bin(int(hexa, 16))[2:]
        return bin_num
    except ValueError:
        return "Error: Invalid hexadecimal number"