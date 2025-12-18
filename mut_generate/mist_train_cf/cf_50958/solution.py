"""
QUESTION:
Write a function named `hex_to_decimal` that takes a hexadecimal string as input and returns its equivalent representation in the base-10 number system. The input hexadecimal string will be in the format "0xXX", where "XX" is the hexadecimal value.
"""

def hex_to_decimal(hex_value):
    return int(hex_value, 16)