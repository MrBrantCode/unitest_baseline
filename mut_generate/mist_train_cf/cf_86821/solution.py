"""
QUESTION:
Design a function `bitwise_sum(a, b)` that computes the sum of two numbers `a` and `b` using only bitwise operations, without using the arithmetic operators `+` and `-`. The function should handle negative numbers, but it can assume the inputs are within the range of a 64-bit signed integer. The function should have a time complexity of O(1) and a space complexity of O(1).
"""

def bitwise_sum(a, b):
    # Iterate until there is no carry left
    while b != 0:
        # Perform bitwise addition without carry
        carry = a & b
        a = a ^ b
        
        # Shift carry by one position to the left
        b = carry << 1

    return a