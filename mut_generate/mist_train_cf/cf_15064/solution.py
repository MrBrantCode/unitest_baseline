"""
QUESTION:
Write a function `add_numbers(a, b)` that computes the sum of two integers `a` and `b` without using the addition operator (+) or any built-in functions that directly perform addition. The function should return the sum of `a` and `b` using a custom algorithm, such as bit manipulation.
"""

def add_numbers(a, b):
    # Iterate until there is no carry
    while b != 0:
        # Calculate the carry
        carry = a & b
        # Calculate the sum without considering the carry
        a = a ^ b
        # Shift the carry to the left by 1 position
        b = carry << 1
    return a