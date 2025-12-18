"""
QUESTION:
Implement a function gcd(a, b) that calculates the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm. The function should take two integers as input and return their GCD. Note that the GCD is the largest positive integer that divides both a and b without leaving a remainder. The function should not use any built-in GCD functions or classes.
"""

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a