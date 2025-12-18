"""
QUESTION:
Implement a function named `decimal_to_binary` to convert a decimal number, including decimal places, to a binary representation using only bitwise operators and without using any built-in functions or libraries to convert the decimal number. The function should handle negative decimal numbers and return a binary representation in two's complement form. Assume the input number is a 32-bit integer.
"""

def decimal_to_binary(num):
    if num == 0:
        return '0'
    elif num < 0:
        # Convert negative number to two's complement form
        num = (1 << 32) + num
    
    binary = ''
    while num > 0:
        binary = str(num % 2) + binary
        num >>= 1
    
    return binary