"""
QUESTION:
Design a function `bitwise_sum(a, b)` that computes the sum of two 32-bit signed integers `a` and `b` using only bitwise operations (AND, XOR, and left shift), without using arithmetic operators + and -. The function should handle negative numbers and produce the correct result within the range of a 32-bit signed integer.
"""

def add(a, b):
    # Iterate until there is no carry left
    while b != 0:
        # Calculate the carry
        carry = a & b

        # Calculate the sum without considering the carry
        a = a ^ b

        # Shift the carry to the left by 1 position
        b = carry << 1

    return a