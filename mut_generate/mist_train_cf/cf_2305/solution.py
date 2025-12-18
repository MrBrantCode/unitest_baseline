"""
QUESTION:
Write a recursive function `sum_primes(n)` that calculates the sum of all prime numbers less than or equal to a given positive integer `n`. The function should have a time complexity of O(n log log n).
"""

def sum_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    if n < 2:
        return 0
    if is_prime(n):
        return n + sum_primes(n-1)
    else:
        return sum_primes(n-1)