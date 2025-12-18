"""
QUESTION:
Implement a function `decimal_to_binary(decimal)` that converts a given decimal number to its binary representation using only bitwise operations. The input decimal number is in the range of 0 to 10^9. The function should return the binary representation as a string.
"""

def entance(decimal):
    binary = ""
    while decimal != 0:
        binary += str(decimal & 1)
        decimal >>= 1
    return binary[::-1]