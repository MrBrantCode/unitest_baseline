"""
QUESTION:
Create a function named `hex_to_bin` that takes a hexadecimal number as input, converts it to decimal, and then converts that decimal number to binary. The function should return the binary representation as a string, excluding the '0b' prefix.
"""

def hex_to_bin(hex_num):
    # Convert hexadecimal to decimal
    dec_num = int(hex_num, 16)
    # Convert decimal to binary
    binary_num = bin(dec_num).replace("0b", "")
    return binary_num