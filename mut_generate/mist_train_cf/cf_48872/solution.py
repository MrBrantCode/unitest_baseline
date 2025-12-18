"""
QUESTION:
Create a function named `hex_to_dec` that takes a two-figure hexadecimal number as input and returns its decimal equivalent. The function should consider the hexadecimal system's base-16 representation and the values of its digits, with A to F corresponding to 10 to 15 in the decimal system. The input hexadecimal number is a string, and the output decimal number is an integer.
"""

def hex_to_dec(hex_val):
    return int(hex_val, 16)