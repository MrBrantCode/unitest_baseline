"""
QUESTION:
Convert a given decimal number to binary. Write a function `decimal_to_binary` that takes a decimal number as input and returns its binary representation as a string. The output should be a string of '0's and '1's.
"""

def decimal_to_binary(n):
    return bin(n)[2:]