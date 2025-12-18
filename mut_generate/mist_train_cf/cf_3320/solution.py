"""
QUESTION:
Create a function `hex_to_bin(hex_num)` that takes a string `hex_num` representing a hexadecimal number and returns its binary equivalent as a string. The function should use bitwise operators for the conversion and not utilize any built-in conversion functions or libraries. The input string `hex_num` will only contain valid hexadecimal digits (0-9 and A-F, uppercase) and can be assumed to be a valid hexadecimal number.
"""

def hex_to_bin(hex_num):
    bin_num = ''
    for char in hex_num:
        dec_num = (ord(char) - 65 + 10) if char.isalpha() else int(char)
        bin_num += bin(dec_num)[2:].zfill(4)
    return bin_num