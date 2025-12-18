"""
QUESTION:
Write a function called `sum_of_primes` that calculates the sum of prime numbers from 0 to n, where n is a given non-negative integer. The function should return the sum of prime numbers.
"""

def sum_of_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    for i in range(n + 1):
        if is_prime(i):
            prime_sum += i
    return prime_sum