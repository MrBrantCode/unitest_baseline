"""
QUESTION:
Create a function `is_power_of_two(n)` to check if a given positive integer `n` is a power of 2 using bitwise operations. The function should have a time complexity of O(1) and a space complexity of O(1). The input `n` should be a positive integer and the output should be a boolean value.
"""

def is_power_of_two(n):
    # Check if n is a positive integer and has exactly one '1' bit set
    return n > 0 and (n & (n - 1)) == 0