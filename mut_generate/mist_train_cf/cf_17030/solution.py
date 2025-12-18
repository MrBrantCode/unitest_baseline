"""
QUESTION:
Write a function decimal_to_binary that takes an integer as input and returns its binary representation as a string. The input integer will be in the range of 0 to 10^9. The function must only use bitwise operations to achieve the conversion.
"""

def decimal_to_binary(decimal):
    binary = ""
    while decimal != 0:
        binary += str(decimal & 1)
        decimal >>= 1
    return binary[::-1]