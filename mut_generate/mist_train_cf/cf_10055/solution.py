"""
QUESTION:
Create a function `increment_by_1(n)` that increments a given non-negative integer `n` by 1 using only bitwise operations. The function should not use any arithmetic operations and should handle the increment operation correctly.
"""

def increment_by_1(n):
    mask = 1
    while n & mask:
        n ^= mask
        mask <<= 1
    n ^= mask
    return n