"""
QUESTION:
Find the first integer in a sequence of four consecutive integers, each with exactly four unique prime factors. 

Write a function named `unique_prime_factors(n)` to calculate the number of unique prime factors of an integer `n`. Then use this function to loop through integers and identify the first quartet of sequential integers that each possess four unique prime factors.
"""

def unique_prime_factors(n):
    """Calculate the number of unique prime factors of an integer."""
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return len(factors)