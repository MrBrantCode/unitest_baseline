"""
QUESTION:
Implement the function `decimal_to_hexadecimal(decimal_num)` to convert a given decimal number to its hexadecimal representation without using any built-in conversion functions or libraries. The function should take an integer `decimal_num` as input and return its hexadecimal representation as a string.
"""

def decimal_to_hexadecimal(decimal_num):
    hex_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 16
        if remainder < 10:
            hex_num = str(remainder) + hex_num
        else:
            hex_num = chr(ord('A') + remainder - 10) + hex_num
        decimal_num //= 16
    return hex_num