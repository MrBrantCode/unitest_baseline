"""
QUESTION:
Create a recursive function called `find_prime_factors` that takes two arguments, `n` and `factor`, to find the prime factors of a given number `n`. The function should start testing factors from 2 and return a list of prime factors.
"""

def find_prime_factors(n, factor=2):
    # Base case: If n is 1, there are no more prime factors
    if n == 1:
        return []

    # If n is divisible by factor, it is a prime factor
    if n % factor == 0:
        return [factor] + find_prime_factors(n // factor, factor)
    
    # If n is not divisible by factor, increment factor and continue recursively
    return find_prime_factors(n, factor + 1)