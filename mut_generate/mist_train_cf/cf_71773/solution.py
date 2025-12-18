"""
QUESTION:
Write a Python function `arithmetic_operation` that takes three arguments, `x`, `y`, and `num`. The function should use a ternary operator to return the sum of `x` and `num` if `x` is greater than `y`, and the difference of `y` and `num` otherwise.
"""

def arithmetic_operation(x, y, num):
    return x + num if x > y else y - num