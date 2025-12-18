"""
QUESTION:
Create a function `decimal_to_binary` that takes an integer `decimal_num` as input and returns its binary representation as a string. The function should not use any built-in functions or libraries for binary conversion. The input will be a non-negative integer, and the output should be a string of binary digits.
"""

def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return '0'
    
    binary_num = ''
    while decimal_num > 0:
        binary_num = str(decimal_num % 2) + binary_num
        decimal_num //= 2
    
    return binary_num