"""
QUESTION:
Write a function `prime_factors_sum(n, divisor=2, result=0)` that calculates the sum of all prime factors of a given positive integer `n` greater than 1. The function must use recursion. The divisor and result parameters are optional, with default values of 2 and 0, respectively.
"""

def prime_factors_sum(n, divisor=2, result=0):
    if n <= 1:
        return result
    elif n % divisor == 0:
        return prime_factors_sum(n // divisor, divisor, result + divisor)
    else:
        return prime_factors_sum(n, divisor + 1, result)