"""
QUESTION:
Create a function `gcd` that takes two positive integers `a` and `b` as input and returns their greatest common divisor (GCD) with a time complexity of O(log(min(a, b))) and a space complexity of O(1). The function should not use any built-in GCD functions or libraries. The input numbers `a` and `b` will not exceed 10^9.
"""

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a