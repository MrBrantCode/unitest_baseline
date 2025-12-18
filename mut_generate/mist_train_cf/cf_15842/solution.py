"""
QUESTION:
Write a function named sum_primes that calculates the sum of all prime numbers from 1 to a given number n (inclusive). Assume n is a positive integer.
"""

def sum_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    for i in range(2, n + 1):
        if is_prime(i):
            prime_sum += i
    return prime_sum