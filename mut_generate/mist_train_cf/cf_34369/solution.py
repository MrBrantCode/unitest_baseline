"""
QUESTION:
Implement the `count_bits` function, which takes an integer `n` as input and returns the number of set bits (binary 1s) in the binary representation of `n`.
"""

def count_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count