"""
QUESTION:
Write a function `prime_factors(n)` that takes an integer `n` as input and returns a list of its prime factors. The function should factorize the input number into a product of its prime factors, and the output should be a list of prime factors without using exponents.
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