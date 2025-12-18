"""
QUESTION:
Implement a function `multiply(a, b)` that calculates the product of two non-negative integers `a` and `b` without using the '*' operator. The function should use bit manipulation and have a time complexity of O(logn) or better, where n is the number of bits in the larger input number.
"""

def multiply(a, b):
    result = 0
    while b != 0:
        if b & 1 == 1:
            result += a
        a <<= 1
        b >>= 1
    return result