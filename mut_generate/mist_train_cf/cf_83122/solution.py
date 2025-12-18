"""
QUESTION:
Implement a function `add_numbers` that takes two integer arguments `x` and `y` and returns their sum using only bitwise operations. The function should be able to handle large input numbers without causing integer overflow.
"""

def add_numbers(x, y):
    while y:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x