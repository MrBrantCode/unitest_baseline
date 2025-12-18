"""
QUESTION:
Write a function `sum_of_distinct_prime_factors(q)` that takes an integer `q` as input and returns the sum of all the distinct prime factors of `q`. The function should iterate through all the prime factors of `q` and ensure distinct values by using a data structure that automatically removes duplicates, such as a set. The function should return the sum of all the distinct prime factors.
"""

def entrance(q):
    factors = set()
    divisor = 2
    while q > 1:
        while q % divisor == 0:
            factors.add(divisor)
            q //= divisor
        divisor += 1
    return sum(factors)