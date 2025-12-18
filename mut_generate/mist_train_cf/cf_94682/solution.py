"""
QUESTION:
Create a function named `add_without_operators` that takes two integers `a` and `b` as input and returns their sum without using any arithmetic operators, bitwise operators, or any other mathematical operations.
"""

def add_without_operators(a, b):
    # base case: if b is 0, return a
    if not b:
        return a
    # recursive case: add the sum of a and b with the carry value
    return add_without_operators(a ^ b, (a & b) << 1)