"""
QUESTION:
Write a function `add_numbers(a, b)` that adds two numbers `a` and `b` using only bitwise operators. The function should take two integers as input and return their sum. Do not use arithmetic operators like `+`, `-`, `*`, `/`, `%`, etc.
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