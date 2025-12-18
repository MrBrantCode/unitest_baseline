"""
QUESTION:
Create a function named `prime_factorization` that takes a positive integer `n` (up to 10^9) as input and returns its prime factorization as a list of tuples, where each tuple consists of a prime number and its corresponding exponent. The prime factorization should be sorted in ascending order based on the prime numbers. The function should optimize the algorithm for prime factorization by only checking prime numbers up to the square root of the input number. If the input number is a prime number itself, it should be included in the output.
"""

import math

def prime_factorization(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def get_prime_numbers(num):
        sieve = [True] * (num + 1)
        sieve[0] = sieve[1] = False
        primes = []
        for p in range(2, int(math.sqrt(num)) + 1):
            if sieve[p]:
                primes.append(p)
                for i in range(p * p, num + 1, p):
                    sieve[i] = False
        for p in range(int(math.sqrt(num)) + 1, num + 1):
            if sieve[p]:
                primes.append(p)
        return primes

    factors = []
    primes = get_prime_numbers(int(math.sqrt(n)))
    for p in primes:
        count = 0
        while n % p == 0:
            n //= p
            count += 1
        if count > 0:
            factors.append((p, count))
    if n > 1:
        factors.append((n, 1))
    return factors