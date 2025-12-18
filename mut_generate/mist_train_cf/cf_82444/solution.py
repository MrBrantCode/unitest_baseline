"""
QUESTION:
Write a function called `prime_factors(n)` that takes an integer `n` as input and returns a list of its prime factors. The function should not use built-in prime functions and should be optimized to handle large numbers efficiently.
"""

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors