"""
QUESTION:
Write a function `add_without_conversion(a, b)` that takes two integers as input and returns their sum using only bitwise operators, without any type conversion.
"""

def add_without_conversion(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a