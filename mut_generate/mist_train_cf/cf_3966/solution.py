"""
QUESTION:
Write a function `calculate_bits(n)` to calculate the number of bits needed to represent the integer `n` in binary form without using any built-in functions or libraries related to binary conversion. The function should take an integer `n` as input and return the number of bits required to represent it in binary form.
"""

def calculate_bits(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 2
    return count