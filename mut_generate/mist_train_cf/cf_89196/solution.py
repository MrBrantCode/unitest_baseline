"""
QUESTION:
Implement a function named `multiply` that takes two non-negative integers `a` and `b` as input and returns their product using bit manipulation, without utilizing the multiplication operator (`*`). The function should have a time complexity of O(logn) or better.
"""

def multiply(a, b):
    result = 0
    while b != 0:
        if b & 1 == 1:
            result += a
        a <<= 1
        b >>= 1
    return result