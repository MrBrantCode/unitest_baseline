"""
QUESTION:
Implement a function named `add_without_operators` that takes two integers `a` and `b` as input and returns their sum. The function should not use any arithmetic operators, bitwise operators, or other mathematical operations.
"""

def add_without_operators(a, b):
    # base case: if b is 0, return a
    if not b:
        return a
    # recursive case: add the sum of a and b with the carry value
    return add_without_operators(a ^ b, (a & b) << 1)