"""
QUESTION:
Create a function `swap_and_multiply` that takes two integers `a` and `b` as arguments. Swap the values of `a` and `b` using a bitwise XOR operation without using any temporary variable, and then multiply `a` by the original value of `b` and return the result.
"""

def swap_and_multiply(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a * b