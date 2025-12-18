"""
QUESTION:
Implement a function `sieve_of_eratosthenes(lower, upper)` that identifies prime numbers within a given integer range `[lower, upper]` efficiently, including handling edge cases where the input range includes numbers less than 2. The function should return a list of prime numbers within the given range.
"""

def sieve_of_eratosthenes(lower, upper):

    sieve = [True] * (upper + 1)
    p = 2
    while p * p <= upper:
        if sieve[p] == True:
            for i in range(p * p, upper + 1, p):
                sieve[i] = False
        p += 1

    primes = []
    for p in range(max(2, lower), upper + 1):  # Include upper limit
        if sieve[p]:
            primes.append(p)

    return primes