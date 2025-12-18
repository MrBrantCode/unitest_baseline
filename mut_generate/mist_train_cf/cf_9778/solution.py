"""
QUESTION:
Create a function named `decimal_to_binary` that takes an integer `decimal_num` as input and returns a string representing the binary representation of the decimal number. The function should not use any built-in functions or libraries for conversion. If the input decimal number is 0, the function should return '0'.
"""

def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return '0'
    
    binary_num = ''
    while decimal_num > 0:
        binary_num = str(decimal_num % 2) + binary_num
        decimal_num //= 2
    
    return binary_num