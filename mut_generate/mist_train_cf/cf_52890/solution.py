"""
QUESTION:
Write a function `count_primes(n)` that takes an integer `n` as input and returns a tuple containing two values: the number of prime numbers less than or equal to `n`, and the number of twin prime pairs less than or equal to `n`. A twin prime pair is a pair of prime numbers that are exactly two numbers apart.

The function should use the Sieve of Eratosthenes algorithm for efficiency and implement caching to store previously computed results to avoid redundant calculations. The function should handle edge cases, including non-integer inputs, negative inputs, and zero inputs, by returning an error message.
"""

def count_primes(n):
    # Edge cases
    if type(n) is not int or n < 0:
        return "Invalid input, please enter a non-negative integer."

    # Algorithm improved with Sieve of Eratosthenes
    sieve = [False, False] + [True for _ in range(2, n+1)]
    p = 2
    while p * p <= n:
        if sieve[p]:
            for i in range(p * p, n+1, p):
                sieve[i] = False
        p += 1

    # Counting primes  
    primes = [i for i, prime in enumerate(sieve) if prime]

    # Counting twin primes
    twin_primes = 0
    for i in range(len(primes)-1):
      if primes[i] + 2 == primes[i+1]:
        twin_primes += 1

    return len(primes), twin_primes