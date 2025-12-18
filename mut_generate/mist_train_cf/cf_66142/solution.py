"""
QUESTION:
Write a function named `hex_product` that calculates the total product of non-zero digits in a given hexadecimal number. The function should take a string representing a hexadecimal number as input, where the string can include digits (0-9) and letters (A-F) representing numbers (10-15). The function should ignore zeros in the calculation.
"""

def hex_product(hex_num):
    hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    product = 1
    for digit in hex_num:
        if digit in hex_dict:
            product *= hex_dict[digit]
        elif int(digit) != 0:
            product *= int(digit)

    return product