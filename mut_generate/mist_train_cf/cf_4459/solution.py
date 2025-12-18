"""
QUESTION:
Implement a recursive function named `list_primes` that prints all prime numbers within a given range without using looping constructs or built-in mathematical functions/libraries. The function should take two parameters, `start` and `end`, representing the range of numbers to check for prime numbers.
"""

def list_primes(start, end, i=2):
    if start > end:
        return
    if start > 1 and is_prime(start, i):
        print(start)
    list_primes(start + 1, end)

def is_prime(n, i=2):
    if n <= 2:
        if n == 2:
            return True
        return False
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)