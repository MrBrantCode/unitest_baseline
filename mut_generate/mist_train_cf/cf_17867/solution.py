"""
QUESTION:
Write a recursive function `prime_factors_sum` that takes a positive integer `n` greater than 1 as input, finds all its prime factors, adds them together, and returns the result. The function should only consider prime factors greater than 1.
"""

def prime_factors_sum(n, divisor=2, result=0):
    if n <= 1:
        return result
    elif n % divisor == 0:
        return prime_factors_sum(n // divisor, divisor, result + divisor)
    else:
        return prime_factors_sum(n, divisor + 1, result)