"""
QUESTION:
Create a function named `prime_factors(n)` that takes an integer `n` as input and returns a list of all the prime factors of `n`. The function should use a trial division approach and return a list of prime factors in any order.
"""

def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        factors.append(n)
    return factors