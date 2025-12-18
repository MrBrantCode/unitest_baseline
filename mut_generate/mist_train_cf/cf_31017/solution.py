"""
QUESTION:
Implement a function `decimal_to_binary` that takes a positive integer `num` as input and returns its binary representation as a string.
"""

def decimal_to_binary(num):
    if num == 0:
        return '0'  
    result = ''
    while num > 0:
        result = str(num % 2) + result  
        num = num // 2  
    return result