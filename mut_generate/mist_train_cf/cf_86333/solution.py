"""
QUESTION:
Implement a function `find_smaller(a, b)` that takes two integers `a` and `b` and returns the smaller one. The function should not use comparison operators, conditional statements, arithmetic operators, bitwise operators (excluding right shift operator), or loops. It should only use basic arithmetic operations and logical operators.
"""

def find_smaller(a, b):
    difference = a - b
    sign = (difference >> 31) & 1
    smaller = sign * a + (1 - sign) * b
    return smaller