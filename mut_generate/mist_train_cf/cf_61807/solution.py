"""
QUESTION:
Design a function named `hex_to_bin_reverse` that takes a string of hexadecimal number as input, converts it to binary, reverses the binary bits, and returns the reversed binary representation as a string. The function should be able to handle large hexadecimal numbers efficiently.
"""

def hex_to_bin_reverse(hex_num):
    # convert hex to binary
    binary_num = bin(int(hex_num, 16))[2:]

    # reverse the bits
    reversed_binary_num = binary_num[::-1]

    return reversed_binary_num