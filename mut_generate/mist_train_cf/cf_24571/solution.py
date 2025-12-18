"""
QUESTION:
Write a function `count_primes(n)` that takes an integer `n` as input and returns the number of prime numbers between 1 and `n`.
"""

def count_primes(n):
    if n <= 2:
        return 0
    sieve = [True] * n
    sieve[0:2] = [False, False]
    for current_prime in range(2, int(n ** 0.5) + 1):
        if sieve[current_prime]:
            for multiple in range(current_prime*2, n, current_prime):
                sieve[multiple] = False
    return sum(sieve)