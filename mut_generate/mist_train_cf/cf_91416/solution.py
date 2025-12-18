"""
QUESTION:
Create a function called `decimal_to_binary` that takes a positive decimal number as input and returns its binary representation as a string using only bitwise operators. The input number is guaranteed to be positive and the function should handle it correctly.
"""

def decimal_to_binary(decimal_number):
    binary = ""
    
    while decimal_number > 0:
        if decimal_number & 1:
            binary += '1'
        else:
            binary += '0'
        decimal_number >>= 1
    
    return binary[::-1]