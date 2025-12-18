"""
QUESTION:
Create a function `print_twin_primes` that takes an integer `limit` as input and prints all pairs of twin prime numbers below the given limit. Twin primes are prime numbers that differ by 2. The function should be able to efficiently handle large inputs and should not take an excessive amount of time or memory to execute.
"""

def entrance(limit):
    def sieve_of_eratosthenes(limit):
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False

        for num in range(2, int(limit ** 0.5) + 1):
            if sieve[num]:
                for multiple in range(num * num, limit + 1, num):
                    sieve[multiple] = False

        return [num for num in range(2, limit) if sieve[num]]

    primes = sieve_of_eratosthenes(limit)

    twin_primes = []
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == 2:
            twin_primes.append((primes[i], primes[i + 1]))

    return twin_primes