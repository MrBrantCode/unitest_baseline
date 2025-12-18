"""
QUESTION:
Write a function `decimal_to_binary(decimal)` that takes a positive integer as input and returns its binary representation as a string. The input decimal number should be less than or equal to 10^9.
"""

def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary