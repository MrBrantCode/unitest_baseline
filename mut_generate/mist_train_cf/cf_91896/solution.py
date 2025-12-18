"""
QUESTION:
Design a function `decimal_to_binary(decimal)` to convert a given decimal number to its binary representation. The function should take an integer `decimal` as input and return the binary string representation. The function should be able to handle the case when the input decimal number is zero, in which case the binary representation will also be zero.
"""

def decimal_to_binary(decimal):
    if decimal == 0:
        return '0'
    
    binary = ''
    while decimal > 0:
        remainder = decimal % 2
        binary += str(remainder)
        decimal //= 2
    
    return binary[::-1]