"""
QUESTION:
Write a function `compute_e` that calculates Euler's number using the infinite series definition: `e = 1/0! + 1/1! + 1/2! + 1/3! + ...`. The function should take an integer `n` as input, representing the number of terms of the series to sum, and return the approximate value of Euler's number.
"""

import math

def compute_e(n):
    e = 0
    for i in range(n):
        e += 1/math.factorial(i)
    return e