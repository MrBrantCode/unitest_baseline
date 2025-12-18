"""
QUESTION:
Implement a function `add_without_arithmetic(a, b)` that takes two 32-bit signed integers `a` and `b` as arguments and returns their sum without using any arithmetic operators or built-in functions. The function should handle negative numbers efficiently, have a time complexity of O(1), and use a constant amount of memory.
"""

def add_without_arithmetic(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1

    return a