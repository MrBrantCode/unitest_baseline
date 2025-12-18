"""
QUESTION:
Implement a function named `decimal_to_binary` that takes a decimal number as input and returns its binary representation as a string. The decimal number is a positive integer and is less than or equal to 10^18.
"""

def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return binary