"""
QUESTION:
Create a function `decimal_to_binary(num)` that takes a decimal number `num` as input and returns its binary representation as a string. The function should be able to handle decimal numbers up to 1,000,000, have a time complexity of O(log(n)), and not use any built-in conversion functions or libraries. The function should also be able to handle negative decimal numbers by adding a '-' sign to the binary representation.
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