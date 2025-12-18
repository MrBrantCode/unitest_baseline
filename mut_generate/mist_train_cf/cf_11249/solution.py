"""
QUESTION:
Write a function named `gcd(a, b)` to calculate the greatest common divisor (GCD) of two integers `a` and `b`. The time complexity of the function should not exceed O(log(min(a, b))) and the space complexity should be O(1).
"""

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)