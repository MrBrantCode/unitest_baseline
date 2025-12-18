"""
QUESTION:
Create a function called `decimal_to_binary` that takes a positive integer less than 1000 as input and returns its binary representation as a string without using any built-in functions or libraries for conversion. The input will always be a positive integer.
"""

def decimal_to_binary(num):
    if num == 0:
        return '0'
    
    binary = ''
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    
    return binary