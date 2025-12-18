"""
QUESTION:
Create a function named `decimal_to_binary` that takes an integer `num` as input and returns its binary representation as a string. The function should be able to handle decimal numbers up to 1,000,000 and have a time complexity of O(log(n)). The function should not use any built-in conversion functions or libraries to convert the decimal number to its binary form and should be able to handle both positive and negative decimal numbers.
"""

def decimal_to_binary(num):
    if num == 0:
        return '0'
    
    binary = ''
    if num < 0:
        binary += '-'
        num = abs(num)
    
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    
    return binary