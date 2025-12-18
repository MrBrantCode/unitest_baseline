"""
QUESTION:
Write a function `sum_of_primes(a, b)` that calculates the sum of all prime numbers within the range `[a, b]` (inclusive) where `a` and `b` are integers. The function should return the sum of prime numbers in the given range.
"""

def sum_of_primes(a, b):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    for num in range(a, b + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum