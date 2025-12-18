"""
QUESTION:
Write a function `bitwise_operation` that takes four variables `a`, `b`, `c`, `d` as input and performs a bitwise operation between `a` and `b` using the bitwise OR operator, assigning the result to `c`. The function should return the value of `c` after the operation. Assume that `a`, `b`, `c`, and `d` are integers.
"""

def bitwise_operation(a, b, c, d):
    c = a | b
    return c