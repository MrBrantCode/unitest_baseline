"""
QUESTION:
Create a function `generate_prime_numbers(start, end)` that generates and returns all prime numbers between `start` and `end` (inclusive). The function should utilize a helper function `is_prime(n)` to check if a number `n` is prime.
"""

def is_prime(n):
    if n <= 1:
       return False
    if n <= 3:
       return True
    if n % 2 == 0 or n % 3 == 0:
       return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime_numbers(start, end):
    primes = []
    for val in range(start, end + 1):
        if is_prime(val):
            primes.append(val)
    return primes