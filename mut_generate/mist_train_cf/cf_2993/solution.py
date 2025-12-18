"""
QUESTION:
Write a function named `gcd` that calculates the Greatest Common Divisor (GCD) of two integers. The function should take two parameters `a` and `b`, and return the GCD as the output. The solution should not use any built-in functions or modules for calculating the GCD. The function should have a time complexity of O(log min(a, b)) and a space complexity of O(1).
"""

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a