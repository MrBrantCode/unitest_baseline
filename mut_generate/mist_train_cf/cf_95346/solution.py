"""
QUESTION:
Write a function named `count_bits` that takes an integer `num` as input and returns the number of bits required to represent it in binary form. The function should not use any built-in functions or libraries related to binary conversion. The input integer `num` can be any positive integer and the function should be able to handle the maximum possible integer.
"""

def count_bits(num):
    count = 0
    while num != 0:
        num //= 2
        count += 1
    return count