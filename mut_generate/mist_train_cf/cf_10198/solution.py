"""
QUESTION:
Create a function `gcd` that calculates the greatest common divisor of two numbers, a and b, with a time complexity of O(log(min(a, b))) and a space complexity of O(1).
"""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a