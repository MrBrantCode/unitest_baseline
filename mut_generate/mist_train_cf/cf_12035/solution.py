"""
QUESTION:
Define a function `add_bitwise(a, b)` that takes two integers `a` and `b` as input and returns their sum using only bitwise operations. The function should not use the arithmetic addition operator (`+`).
"""

def add_bitwise(a, b):
    while b:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a