"""
QUESTION:
Write a function named `prime_factors` that takes an integer `n` as input and returns its prime factors. The function should return a list of prime factors.
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