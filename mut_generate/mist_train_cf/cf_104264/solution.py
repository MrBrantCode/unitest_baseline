"""
QUESTION:
Write a function `calculateSum(a, b)` to recursively calculate the sum of two positive integers `a` and `b` without using the addition operator (+) or any other arithmetic operators. The function should not use any built-in functions or external libraries.
"""

def add(x, y):
    if y == 0:
        return x
    else:
        return add(x ^ y, (x & y) << 1)