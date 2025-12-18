"""
QUESTION:
Write a function `decimal_to_octal(decimal)` to convert a given decimal number to its octal representation using only bitwise operators. The function should take an integer `decimal` as input and return the octal representation as an integer. Note that the function should not use any built-in conversion functions or libraries.
"""

def decimal_to_octal(decimal):
    if decimal == 0:
        return 0

    result = 0
    power = 1

    while decimal != 0:
        result |= (decimal & 0b111) * power
        decimal >>= 3
        power *= 10

    return result