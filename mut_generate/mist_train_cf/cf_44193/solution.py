"""
QUESTION:
Write a function `find_primes(n)` that returns a list of all prime numbers up to the given integer `n`. The function should utilize a helper function `is_prime(n)` to check whether a number is prime or not. The `is_prime(n)` function should return `True` if the number is prime, `False` otherwise.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(n):
    primes = []
    for i in range(n+1):
        if is_prime(i):
            primes.append(i)
    return primes