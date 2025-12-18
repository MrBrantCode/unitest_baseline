"""
QUESTION:
Write a function `sum_of_primes(n)` to calculate the sum of all prime numbers up to the given number `n`. The function should take an integer `n` as input and return the sum of all prime numbers less than or equal to `n`.
"""

def sum_of_primes(n):
    sieve = [True] * (n+1)
    sieve[0:2] = [False, False]
    for currentPrime in range(2, int(n ** 0.5) + 1):
        if sieve[currentPrime] is True:
            for multiple in range(currentPrime * currentPrime, n + 1, currentPrime):
                sieve[multiple] = False
    primes = [prime for prime, checked in enumerate(sieve) if checked is True]
    return sum(primes)