"""
QUESTION:
Write a function `decimal_to_binary` that takes a decimal number as input and returns its binary representation as a string. The function should use the division by 2 method to convert the decimal number to binary notation.
"""

def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary