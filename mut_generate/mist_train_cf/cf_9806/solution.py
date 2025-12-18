"""
QUESTION:
Write a function `sum_of_primes(n)` to find the sum of all prime numbers from 2 to `n`. The function should take an integer `n` as input and return the sum of all prime numbers within the range 2 to `n` (inclusive).
"""

def sum_of_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes_sum = 0
    for i in range(2, n + 1):
        if is_prime(i):
            primes_sum += i
    return primes_sum