"""
QUESTION:
Write a function `calculate_sum(n)` that calculates the sum of the first n terms of the mathematical series x = 2^n / (n!), where n is a positive integer. The function should return the sum as a float value.
"""

import math

def calculate_sum(n):
    sum = 0
    for i in range(1, n + 1):
        term = math.pow(2, i) / math.factorial(i)
        sum += term
    return sum