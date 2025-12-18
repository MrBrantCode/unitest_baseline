"""
QUESTION:
Write a function `calculate_parity(n)` to calculate the parity of a given non-negative integer `n` using only bitwise operations. The function should return 1 if the number of set bits in the binary representation of `n` is odd, and 0 if it is even.
"""

def calculate_parity(n):
    parity = 0
    while n:
        parity ^= n & 1
        n >>= 1
    return parity