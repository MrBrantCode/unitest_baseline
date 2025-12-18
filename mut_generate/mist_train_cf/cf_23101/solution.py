"""
QUESTION:
Write a function `prime_sum(n)` that calculates and returns the sum of all prime numbers from 2 to `n`, where `n` is a given integer greater than 1.
"""

def prime_sum(n):
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