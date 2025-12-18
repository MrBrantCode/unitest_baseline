"""
QUESTION:
Implement a function named `decimal_to_binary` that takes a positive integer as input and returns its binary representation as a string. The input integer should be less than or equal to 10^18.
"""

def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return binary