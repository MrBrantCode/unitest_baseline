"""
QUESTION:
Write a function `calculate_exponential(x, n)` that calculates the exponential of a number `x` using the Taylor series expansion. The function should take two arguments: `x` (the number for which to calculate the exponent) and `n` (the number of terms in the Taylor series to sum over).
"""

def calculate_exponential(x, n):
    exp = 1.0
    power = 1
    fact = 1
    for i in range(1, n+1):
        power = power * x
        fact = fact * i
        exp += power / fact
    return exp