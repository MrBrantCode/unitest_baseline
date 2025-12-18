"""
QUESTION:
Write a function named `find_prime_sum` that takes an integer `n` as input and returns the sum of all prime numbers up to `n`. The input `n` is a positive integer.
"""

def find_prime_sum(n):
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