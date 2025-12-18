"""
QUESTION:
Write a function `is_prime(num)` to check if a number is prime, and another function `get_primes(n)` that generates and returns the first 'n' prime numbers in reverse order. The `is_prime(num)` function should return a boolean value indicating whether 'num' is prime or not. The `get_primes(n)` function should use the `is_prime(num)` helper function to generate the prime numbers and return them in reverse order.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return list(reversed(primes))