"""
QUESTION:
Write a function `print_twin_primes(limit)` that prints all pairs of twin prime numbers below the given limit, where twin primes are prime numbers that differ by 2. The function should efficiently handle large inputs without excessive time or memory usage.
"""

def print_twin_primes(limit):
    def sieve_of_eratosthenes(limit):
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False

        primes = []
        for num in range(2, int(limit ** 0.5) + 1):
            if sieve[num]:
                primes.append(num)
                for multiple in range(num * num, limit + 1, num):
                    sieve[multiple] = False

        for num in range(int(limit ** 0.5) + 1, limit + 1):
            if sieve[num]:
                primes.append(num)

        return primes

    primes = sieve_of_eratosthenes(limit)

    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == 2:
            print((primes[i], primes[i + 1]))