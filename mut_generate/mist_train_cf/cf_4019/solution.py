"""
QUESTION:
Write a function named `decimal_to_binary` that takes an integer `num` as input and returns its binary representation using only bitwise operations and without using any built-in functions or libraries. The time complexity of this function should be O(log n), where n is the decimal number.
"""

def decimal_to_binary(num):
    if num == 0:
        return 0
    
    binary = 0
    place = 1
    
    while num != 0:
        binary += (num % 2) * place
        num >>= 1
        place *= 10
    
    return binary