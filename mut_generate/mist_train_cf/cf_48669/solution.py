"""
QUESTION:
Develop a recursive function named `recursive_prime_factors` that determines the prime factors of a given number. The function should take two parameters: the number to be factorized and an optional list of factors (defaulting to an empty list). The function should return a list of prime factors of the given number.
"""

def recursive_prime_factors(n, factors=[]):
    # smallest prime number
    if n == 1:
        return factors

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return recursive_prime_factors(n/i, factors+[i])

    # when n is prime
    return factors + [n]