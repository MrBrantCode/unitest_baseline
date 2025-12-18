"""
QUESTION:
Write a function `sum_primes` that takes two input parameters: `start` and `end` values, and returns the sum of the first 100 prime numbers between the `start` and `end` values (inclusive). The function should use the Sieve of Eratosthenes algorithm to generate prime numbers within the given range, and check that the `start` and `end` values are positive integers and that the `start` value is smaller than or equal to the `end` value.
"""

def sum_primes(start, end):
    """
    Calculates the sum of the first 100 prime numbers between start and end (inclusive).
    Uses the Sieve of Eratosthenes algorithm to generate prime numbers.
    """
    if not isinstance(start, int) or not isinstance(end, int):
        return 0
    if start <= 0 or end <= 0:
        return 0
    if start > end:
        return 0
    
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