"""
QUESTION:
Implement a function named `decimal_to_binary` that takes an integer as input and returns its binary representation as a string. The function should handle both positive and negative integers, and negative integers should be converted to their two's complement form. The function should use only bitwise operators and not any built-in functions or libraries to convert the decimal number. Assume that we are working with 32-bit integers.
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