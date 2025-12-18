"""
QUESTION:
Write a function `sum_of_primes_in_range` that calculates the sum of all prime numbers within a given range from `start` to `end` (inclusive), where `start` and `end` are positive integers.
"""

def sum_of_primes_in_range(start, end):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    for num in range(start, end + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum