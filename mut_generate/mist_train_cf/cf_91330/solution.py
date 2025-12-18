"""
QUESTION:
Write a function named `decimal_to_octal` that takes an integer as input and returns its octal representation as an integer, using only bitwise operators for the conversion. The function should handle the case where the input is 0, and return 0 in this case.
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