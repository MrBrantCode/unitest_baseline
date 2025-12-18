"""
QUESTION:
Write a function `is_power_of_two` that checks if a given integer `n` is a power of 2, represented in binary with exactly one '1' bit set. The function should have a time complexity of O(1) and a space complexity of O(1).
"""

def is_power_of_two(n):
    # Check if n is a positive integer and has exactly one '1' bit set
    return n > 0 and (n & (n - 1)) == 0