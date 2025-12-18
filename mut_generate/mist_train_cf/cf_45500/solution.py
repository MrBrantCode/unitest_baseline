"""
QUESTION:
Create a function `decimal_to_binary(num)` that takes a positive integer as input and returns its binary representation as a string. The function should be able to handle any arbitrary positive integer.
"""

def decimal_to_binary(num):
    binary = []
    while num > 0:
        binary.append(str(num % 2))
        num = num // 2
    return ''.join(binary[::-1])