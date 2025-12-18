"""
QUESTION:
Implement a function named "gcd" that takes two integer arguments a and b and returns their greatest common divisor (GCD) using the Euclidean algorithm. The function should not use any built-in functions or libraries for finding the GCD. The GCD is the largest positive integer that divides both a and b without leaving a remainder.
"""

def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a