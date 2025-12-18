"""
QUESTION:
Write a function `calculate_hdn(n)` that calculates the harmonic divisor number (HDN) of a given positive integer `n`. The HDN of `n` is defined as the sum of the reciprocals of each of its divisors. The function should take a positive integer `n` as input and return the HDN of `n` rounded to two decimal places.
"""

def calculate_hdn(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    hdn = sum(1 / divisor for divisor in divisors)
    return round(hdn, 2)