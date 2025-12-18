"""
QUESTION:
Write a function `sumOfPrimes` that calculates the sum of all prime numbers up to a given integer `n`, where `n` is a natural number greater than 1. The function should take an integer `n` as input and return the sum of all prime numbers up to and including `n`. The input `n` is guaranteed to be a positive integer.
"""

def sumOfPrimes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    for i in range(2, n + 1):
        if is_prime(i):
            prime_sum += i
    return prime_sum