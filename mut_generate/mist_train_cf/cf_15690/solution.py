"""
QUESTION:
Implement a recursive function `gcd_recursive` that calculates the greatest common divisor of two integers. The function should have a time complexity of O(log min(n1, n2)), should not use any built-in functions or libraries, and should handle negative integers as input.
"""

def gcd_recursive(a, b):
    if a == 0:
        return abs(b)
    if b == 0:
        return abs(a)
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    return gcd_recursive(b % a, a)