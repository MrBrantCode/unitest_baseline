"""
QUESTION:
Write a function `generate_primes` that returns a list of the first 5 prime numbers excluding any prime numbers that are palindromic and have a prime number of digits.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_palindromic(n):
    return str(n) == str(n)[::-1]

def generate_primes():
    prime_numbers = [x for x in range(2, 1000) if is_prime(x)]
    return [x for x in prime_numbers if not is_palindromic(x) and not is_prime(len(str(x)))][:5]