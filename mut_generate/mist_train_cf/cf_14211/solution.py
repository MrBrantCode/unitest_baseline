"""
QUESTION:
Implement a function `decimal_to_hexadecimal` that takes a decimal number as input and returns its hexadecimal representation as a string. The function should not use any built-in conversion functions or libraries. The hexadecimal representation should use uppercase letters for digits greater than 9.
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