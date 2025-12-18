"""
QUESTION:
Write a function `sum_of_primes(n)` that calculates the sum of all prime numbers between 2 and `n` (inclusive), where `n` is a non-negative integer.
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
    for num in range(2, n + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum