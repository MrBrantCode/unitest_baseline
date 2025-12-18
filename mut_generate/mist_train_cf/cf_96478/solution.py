"""
QUESTION:
Write a function `add(x, y)` that adds two integers `x` and `y` without using the "+" operator or any type conversion, using only bitwise operators.
"""

def add(x, y):
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x