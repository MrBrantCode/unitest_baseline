"""
QUESTION:
Write a recursive function `sum_of_primes(n)` to calculate the sum of all prime numbers from 1 to a given positive integer `n`. The function should use a helper function `is_prime(m)` to check whether a number `m` is prime or not. The function should return 0 if `n` is less than 2, since there are no prime numbers less than 2. The `is_prime` function should return `True` if a number is prime and `False` otherwise.
"""

def is_prime(m):
    if m < 2:
        return False
    for i in range(2, int(m**0.5) + 1):
        if m % i == 0:
            return False
    return True

def sum_of_primes(n):
    if n < 2:
        return 0
    elif is_prime(n):
        return n + sum_of_primes(n-1)
    else:
        return sum_of_primes(n-1)