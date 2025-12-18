"""
QUESTION:
Write a function `sum_of_primes` that calculates and returns the sum of all prime numbers up to and including a given number `n`. The input `n` is an integer and `n >= 1`.
"""

def sum_of_primes(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    return sum(i for i in range(2, n + 1) if is_prime(i))