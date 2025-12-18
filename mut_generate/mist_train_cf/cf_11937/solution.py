"""
QUESTION:
Write a function `sum_of_primes(n)` that calculates the sum of all prime numbers between 1 and `n` (inclusive) recursively, where `n` is a positive integer. Assume that `n` is a valid input and will not be checked for validity within the function.
"""

def sum_of_primes(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    if n <= 1:
        return 0
    if is_prime(n):
        return n + sum_of_primes(n-1)
    else:
        return sum_of_primes(n-1)