"""
QUESTION:
Implement a function named `gcd` that takes two integers `a` and `b` as inputs and returns their greatest common divisor using the Euclidean Algorithm with a time complexity of O(log(min(a,b))) and a space complexity of O(1).
"""

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)