"""
QUESTION:
Write a function `countSetBits` to count the number of set bits (binary 1s) in the binary representation of a non-negative integer `A`. The function should take an integer `A` as input and return the count of set bits in its binary representation.
"""

def countSetBits(A: int) -> int:
    num = 0
    while A:
        num += A & 1
        A = A >> 1
    return num