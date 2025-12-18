"""
QUESTION:
Create a function named `increment_by_1` that increments a given non-negative integer `n` by 1 using only bitwise operations. The function must not use any arithmetic operations.
"""

def increment_by_1(n):
    mask = 1
    while n & mask:
        n ^= mask
        mask <<= 1
    n ^= mask
    return n