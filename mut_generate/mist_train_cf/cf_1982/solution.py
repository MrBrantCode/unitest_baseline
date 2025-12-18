"""
QUESTION:
Write a recursive function `add_numbers_recursive(a, b)` that adds two integers `a` and `b` without using any arithmetic operators or built-in functions specifically designed for addition. The function should use bitwise operators instead and handle all possible input values.
"""

def add_numbers_recursive(a, b):
    if b == 0:
        return a
    else:
        sum = a ^ b  # Perform bitwise XOR to get the sum of bits without carry
        carry = (a & b) << 1  # Perform bitwise AND and left shift to get the carry
        return add_numbers_recursive(sum, carry)