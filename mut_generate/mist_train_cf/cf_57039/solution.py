"""
QUESTION:
Write a function called `find_prime_factors` that takes an integer `n` as input and returns a list of its prime factors. The function should only consider factors up to the square root of `n` and return all prime factors, including duplicates. The input number `n` is a positive integer greater than 1.
"""

def find_prime_factors(n):
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