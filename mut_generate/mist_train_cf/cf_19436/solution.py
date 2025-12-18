"""
QUESTION:
Compute the sum of two integers without using the "+" operator, mathematical operators, or bitwise operators other than XOR (^) and AND (&). The solution should have a time complexity of O(log n), where n is the maximum number of bits required to represent the given integers.

The function should take two integers as input and return their sum. 

The function name should be sum_without_operator(x, y).
"""

def sum_without_operator(x, y):
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x