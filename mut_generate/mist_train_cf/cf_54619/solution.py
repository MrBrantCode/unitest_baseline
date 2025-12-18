"""
QUESTION:
Write a Python function named `sum_of_squares_of_primes(n)` that calculates the sum of squares of all prime numbers less than or equal to `n`. The function should take an integer `n` as input and return the sum of squares of all prime numbers up to `n`.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_squares_of_primes(n):
    sum_ = 0
    for i in range(2, n + 1):
        if is_prime(i):
            sum_ += i**2
    return sum_