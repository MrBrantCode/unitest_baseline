"""
QUESTION:
Create a function `prime_numbers` that generates a list of all prime numbers from 2 to a given integer `n`, where `n` is greater than 1. The function should return a list of integers.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(n):
    primes = []
    for num in range(2, n+1):
        if is_prime(num):
            primes.append(num)
    return primes