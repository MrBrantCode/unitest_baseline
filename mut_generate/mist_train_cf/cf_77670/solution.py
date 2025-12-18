"""
QUESTION:
Create a function named `sum_of_primes(n)` that calculates the sum of all distinct prime numbers that result from different combinations of ascending a staircase with 'n' steps. Each step can be either 1 or 2 steps at a time. The function should be able to handle large inputs efficiently.
"""

from itertools import combinations
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(n):
    unique_primes = set()
    for i in range(1, n//2+1): 
        for c in combinations(range(1, n + 1), i):
            if sum(c) == n and is_prime(len(c)):
                unique_primes.add(len(c))
    return sum(unique_primes)