"""
QUESTION:
Write a function `count_bits(num)` that calculates the number of bits needed to represent a given integer `num` in binary form without using any built-in functions or libraries related to binary conversion. The function should return the number of bits required. The input `num` will be a non-negative integer.
"""

def count_bits(num):
    count = 0
    while num != 0:
        num //= 2
        count += 1
    return count