"""
QUESTION:
Implement a function "gcd" that takes two integers as input and returns their greatest common divisor using only iterative methods. The function should not use any built-in functions or libraries for finding the greatest common divisor.
"""

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        remainder = a % b
        a, b = b, remainder
    return a