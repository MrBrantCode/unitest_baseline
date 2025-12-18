"""
QUESTION:
Create a function `prime_factors(n)` that calculates the prime factors of a given positive integer `n`. The function should return a list of prime factors in the order they are obtained. The input `n` is a positive integer and the output should be a list of integers.
"""

def prime_factors(n):
    factors = []
    divisor = 2
    while(divisor <= n):
        if (n % divisor) == 0:
            factors.append(divisor)
            n = n / divisor
        else:
            divisor += 1
    return factors