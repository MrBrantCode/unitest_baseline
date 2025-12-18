"""
QUESTION:
Create a function `add_numbers(a, b)` that takes two integers as input and returns their sum without using the `+` or `-` operators. The function should be able to handle any two integers provided and accommodate for overflow and underflow issues.
"""

def add_numbers(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a