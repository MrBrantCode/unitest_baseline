"""
QUESTION:
Implement a function `gcd(a, b)` that calculates the greatest common divisor of two integers `a` and `b` using the Euclidean Algorithm with a recursive approach and no loops. The function should have a time complexity of O(log(min(a, b))) and a space complexity of O(1), without using any additional data structures.
"""

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)