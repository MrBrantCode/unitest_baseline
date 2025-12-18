"""
QUESTION:
Write a function `sum_primes(start, end)` that calculates the sum of the first 100 prime numbers between `start` and `end` (inclusive) using the Sieve of Eratosthenes algorithm. The function should take two input parameters, `start` and `end`, which are positive integers where `start` is smaller than or equal to `end`. The function should return the sum of the first 100 prime numbers in the given range. If there are less than 100 prime numbers in the range, return the sum of all prime numbers in the range.
"""

def sum_primes(start, end):
    """
    Calculates the sum of the first 100 prime numbers between start and end (inclusive).
    Uses the Sieve of Eratosthenes algorithm to generate prime numbers.
    """
    # Generate prime numbers using Sieve of Eratosthenes algorithm
    primes = []
    sieve = [True] * (end+1)
    sieve[0] = False
    sieve[1] = False
    
    for i in range(2, int(end**0.5)+1):
        if sieve[i]:
            for j in range(i**2, end+1, i):
                sieve[j] = False
    
    for i in range(start, end+1):
        if sieve[i]:
            primes.append(i)
    
    if len(primes) < 100:
        return sum(primes)
    else:
        return sum(primes[:100])