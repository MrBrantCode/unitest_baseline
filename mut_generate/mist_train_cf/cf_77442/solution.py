"""
QUESTION:
Create a function `hex_to_bin(hex_value)` that takes a string `hex_value` representing a hexadecimal number as input and returns its equivalent binary representation as a string. The function should handle potential errors and return the error message as a string. The input hexadecimal number should be converted to decimal using base 16 before being converted to binary. The "0b" prefix from the binary conversion should be removed from the output.
"""

def hex_to_bin(hex_value):
    try:
        bin_value = bin(int(hex_value, 16))[2:]
        return bin_value
    except Exception as e:
        return str(e)