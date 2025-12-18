"""
QUESTION:
Write a function named `prime_factors` that takes an integer `n` as input and returns a list of its prime factors. The function should be able to handle positive integers. For example, `prime_factors(100)` should return `[2, 2, 5, 5]`.
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