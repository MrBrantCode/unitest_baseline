"""
QUESTION:
Write a function `get_sum(a, b)` that calculates the sum of two integers `a` and `b` without using the `+` or `-` operators. The function should have a time complexity of O(log n), where n is the larger of the two integers.
"""

def get_sum(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a