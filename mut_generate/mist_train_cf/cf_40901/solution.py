"""
QUESTION:
Implement the `erfc`, `lgamma`, and `tgamma` functions in Python, each taking a single floating-point number as input. The `erfc` function should return its complementary error function value, the `lgamma` function should return the natural logarithm of the absolute value of the gamma function, and the `tgamma` function should return the gamma function value. Use the math module for implementation and ensure accurate results for various input values.
"""

import math

def erfc(x):
    return 1 - math.erf(x)

def lgamma(x):
    return math.lgamma(x)

def tgamma(x):
    return math.gamma(x)