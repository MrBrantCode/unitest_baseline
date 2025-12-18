"""
QUESTION:
Write a function named prime_factors() that finds all the prime factors of a given integer and returns them along with their multiplicities. The function should be able to handle integers up to 10^9.
"""

def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return {factor: factors.count(factor) for factor in set(factors)}