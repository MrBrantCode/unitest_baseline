"""
QUESTION:
Implement a function `decimal_to_binary(decimal)` that converts a decimal number to binary using only bitwise operators and without using any loops or recursion. The function should handle both positive and negative integers as input and return their binary representation as a string.
"""

def decimal_to_binary(decimal):
    is_negative = False
    if decimal < 0:
        is_negative = True
        decimal = abs(decimal)

    binary = ""
    if decimal == 0:
        binary = "0"

    while decimal > 0:
        bit = decimal & 1
        binary = str(bit) + binary
        decimal = decimal >> 1

    if is_negative:
        binary = "-" + binary

    return binary