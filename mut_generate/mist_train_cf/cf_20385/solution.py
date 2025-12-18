"""
QUESTION:
Implement a function named `decimal_to_binary(decimal)` that converts a given decimal number, including decimal places, to its binary representation. The function should use only bitwise operators and not use any built-in functions or libraries to convert the decimal number. Additionally, it should handle negative decimal numbers and return a binary representation in two's complement form. The function should take an integer as input and return a string representing the binary representation of the decimal number.
"""

def entance(decimal):
    if decimal == 0:
        return '0'

    binary = ''
    negative = False

    if decimal < 0:
        negative = True
        decimal = abs(decimal)

    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2

    if negative:
        binary = '-' + binary

    return binary