"""
QUESTION:
Write a recursive function `list_primes(start, end)` that prints all prime numbers within the range defined by `start` and `end` without using any looping constructs or built-in mathematical functions/libraries. The function should utilize a helper function `is_prime(n)` to check if a number `n` is prime.
"""

def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)

def list_primes(start, end):
    if start <= end:
        if is_prime(start):
            print(start)
        list_primes(start + 1, end)