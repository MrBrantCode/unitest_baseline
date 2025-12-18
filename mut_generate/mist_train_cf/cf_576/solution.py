"""
QUESTION:
Write a function `multiply_subtract_sum(a, b)` that calculates the sum of two numbers `a` and `b` using only multiplication and subtraction operations, with a time complexity of O(1).
"""

def multiply_subtract_sum(a, b):
    return (a * (b // 5)) - (b % 5)