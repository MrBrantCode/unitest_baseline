"""
QUESTION:
Write a function `print_and_sum_primes(n)` that prints the first 1000 prime numbers and returns the sum of these prime numbers. The input `n` should be used to determine the limit of the prime number generation, and the function should have a time complexity of O(n^2), where `n` is the value of the 1000th prime number.
"""

def print_and_sum_primes(n):
    def sieve_of_eratosthenes(limit):
        primes = [True] * (limit + 1)
        primes[0] = primes[1] = False

        for i in range(2, int(limit ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, limit + 1, i):
                    primes[j] = False

        return [i for i in range(limit + 1) if primes[i]]

    primes = sieve_of_eratosthenes(n * n)
    count = 0
    total_sum = 0

    for prime in primes:
        if count == 1000:
            break

        if prime > 1:
            print(prime)
            total_sum += prime
            count += 1

    return total_sum