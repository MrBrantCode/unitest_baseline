"""
QUESTION:
Create a function called `prime_factors(n)` that returns a list of all prime factors of a given number `n`. The function should take an integer `n` as input and return a list of integers representing the prime factors. There are no restrictions on the input values of `n`, but the function should be able to handle any positive integer.
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