"""
QUESTION:
Write a function `gcd(a, b)` to calculate the greatest common divisor (GCD) of two integers `a` and `b` without using any built-in mathematical functions or libraries. The function should handle both non-negative and negative integers. The time complexity of the solution should be O(log(min(a,b))).
"""

def gcd(a, b):
    # Handle negative inputs
    a = abs(a)
    b = abs(b)

    # Base cases
    if a == 0:
        return b
    if b == 0:
        return a

    # Reduce the problem to smaller subproblems
    if a > b:
        return gcd(b, a % b)
    else:
        return gcd(a, b % a)