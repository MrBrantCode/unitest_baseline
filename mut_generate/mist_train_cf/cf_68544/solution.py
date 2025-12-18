"""
QUESTION:
Write a function named `hex_to_decimal` that takes a list of hexadecimal strings as input and returns a list of their decimal integer equivalents. The function should convert each hexadecimal string to a decimal integer using base 16.
"""

def hex_to_decimal(hex_list):
    decimal_list = []
    for hex_num in hex_list:
        decimal_num = int(hex_num, 16)
        decimal_list.append(decimal_num)
    return decimal_list