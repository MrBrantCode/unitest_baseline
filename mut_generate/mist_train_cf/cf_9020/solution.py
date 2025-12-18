"""
QUESTION:
Write a function `binary_to_decimal(binary)` that takes a binary string as input and returns its corresponding decimal number without using any built-in functions or libraries for converting binary to decimal.
"""

def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2
        if digit == '1':
            decimal = decimal + 1
    return decimal