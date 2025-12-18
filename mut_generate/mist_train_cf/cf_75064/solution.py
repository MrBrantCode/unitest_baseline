"""
QUESTION:
Write a function `compute_e` that takes an integer `precision` as input and returns an approximation of Euler's number calculated up to the specified number of terms in the infinite series.
"""

import math

def compute_e(precision):
    e = 2
    fact = 2
    for i in range(2, precision+1):
        fact *= i
        e += 1/fact
    return e