"""
QUESTION:
Write a function called `simplify_fraction` that takes two integers as input, `numerator` and `denominator`, and returns their simplified fraction. The function should calculate the greatest common divisor (GCD) of the two numbers and divide both the numerator and denominator by the GCD. The function should return the simplified fraction as a string in the format "numerator/denominator". The input numbers are guaranteed to be positive integers.
"""

import math

def simplify_fraction(numerator, denominator):
    gcd = math.gcd(numerator, denominator)
    return f"{numerator//gcd}/{denominator//gcd}"