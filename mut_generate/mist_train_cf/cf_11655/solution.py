"""
QUESTION:
Design a function named `gcd` that takes two integers `a` and `b` as input and returns their greatest common divisor without using any built-in functions or libraries. The function should use a while loop to implement the Euclidean algorithm from scratch.
"""

def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a