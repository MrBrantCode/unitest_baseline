"""
QUESTION:
Write a function `hammingWeight(n)` that takes an unsigned 32-bit integer represented as a binary string `n` and returns a list containing the number of '1' bits and the number of '0' bits in `n`.
"""

def hammingWeight(n: str) -> list:
    ones = bin(int(n, 2)).count("1")
    zeros = 32 - ones
    return [ones, zeros]