"""
QUESTION:
Write a function `findMax` that takes two integers `a` and `b` as input and returns the maximum value among them. The function should not use comparison operators (`>`, `<`, `==`) or ternary operators.
"""

def findMax(a, b):
    diff = a - b
    sign = (diff >> 31) & 0x1  # Extracting the sign bit (0 for positive, 1 for negative)
    return a - diff * sign  # If a is greater, sign is 0 and a - 0 * diff = a; if b is greater, sign is 1 and a - 1 * diff = a - diff = b