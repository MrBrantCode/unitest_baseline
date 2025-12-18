"""
QUESTION:
Create a function `gcd(a, b)` that finds the greatest common divisor (GCD) of two integers `a` and `b` with a time complexity of O(log(min(a,b))) and a space complexity of O(1). The function should take two integers `a` and `b` as input and return their GCD.
"""

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)