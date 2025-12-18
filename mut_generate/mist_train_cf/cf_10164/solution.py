"""
QUESTION:
Implement the "add_two_numbers" function, which takes two integers as input and returns their sum without using the "+" operator or any built-in functions for addition. The function should only use bitwise operators.
"""

def add_two_numbers(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a