"""
QUESTION:
Implement the function `add_two_numbers(a, b)` that takes two integers `a` and `b` as input and returns their sum using bitwise operations.
"""

def add_two_numbers(a, b):
    '''This function takes two numbers and returns their sum using bitwise operations.'''
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a