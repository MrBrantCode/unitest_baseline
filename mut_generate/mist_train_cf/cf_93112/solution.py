"""
QUESTION:
Write a function `hex_to_decimal(hex_num)` that takes a string representing a hexadecimal number as input and returns its corresponding decimal representation. The input hexadecimal number is a string of characters 0-9 and A-F (case insensitive), and the function should return an integer.
"""

def hex_to_decimal(hex_num):
    decimal_num = int(hex_num, 16)
    return decimal_num