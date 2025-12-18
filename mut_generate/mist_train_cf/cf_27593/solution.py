"""
QUESTION:
Write a function `count_set_bits(n)` that takes an integer `n` as input and returns the remainder when the count of set bits (1s) in its binary representation is divided by 3. The function should not take any other input and should not have any side effects. The input integer `n` is non-negative.
"""

def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count % 3