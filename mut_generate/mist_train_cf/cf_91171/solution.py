"""
QUESTION:
Implement a function `add_numbers(a, b)` that takes two integers `a` and `b` as input and returns their sum using only bitwise operators. The function should not use arithmetic operators like `+` or `-` and should only use bitwise operators such as `&`, `^`, `<<`, etc.
"""

def add_numbers(a, b):
    while b != 0:
        # Calculate the carry
        carry = a & b

        # Add the bits without carry
        a = a ^ b

        # Shift the carry by one position
        b = carry << 1

    return a