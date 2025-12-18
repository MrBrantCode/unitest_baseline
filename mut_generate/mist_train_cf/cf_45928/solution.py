"""
QUESTION:
Implement a function `compute_euler(n)` that calculates Euler's number using the sum of the reciprocal of n factorial for n terms, where n is the number of terms used in the series. The function should return the calculated value of Euler's number.
"""

import math

def compute_euler(n):
    euler = sum(1 / math.factorial(i) for i in range(n))
    return euler