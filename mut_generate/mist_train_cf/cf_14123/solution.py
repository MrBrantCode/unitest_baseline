"""
QUESTION:
Write a function `bitwise_operations(a, b)` that takes in two integers `a` and `b` and returns a list containing their bitwise AND, OR, and XOR results in that order.
"""

def bitwise_operations(a, b):
    bitwise_and = a & b
    bitwise_or = a | b
    bitwise_xor = a ^ b
    
    return [bitwise_and, bitwise_or, bitwise_xor]