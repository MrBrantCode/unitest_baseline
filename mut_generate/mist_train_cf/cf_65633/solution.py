"""
QUESTION:
Write a function named `calculate_euler_number` that uses the infinite series definition to approximate Euler's number. The function should take one argument `num_terms`, which represents the number of terms to include in the series. The function should return the approximated value of Euler's number.
"""

import math

def calculate_euler_number(num_terms):
    e = 0
    for i in range(num_terms):
        e += 1 / math.factorial(i)
    return e