"""
QUESTION:
Design a function `bitwise_sum(a, b)` that takes two integers `a` and `b` as input and returns their sum, but only using bitwise operations. The function should not use arithmetic operators for addition.
"""

def bitwise_sum(a, b):
    while b != 0:
        carry = a & b  # carry is the common set bits of a and b
        a = a ^ b     # sum of bits without considering carry
        b = carry << 1  # carry is shifted by one bit to the left
    return a