"""
QUESTION:
Write a function `binary_capacity(bit_count)` that calculates the unique identification capacity of an n-bit binary sequence. The function should take an integer `bit_count` as input and return the total number of unique combinations possible with that number of bits. Assume that each bit can have a value of 0 or 1, and the function should be able to handle any non-negative integer value of `bit_count`.
"""

def binary_capacity(bit_count):
    return 2**bit_count