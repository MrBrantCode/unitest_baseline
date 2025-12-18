"""
QUESTION:
Write a function `is_prime(num)` to check if a given number `num` is prime, `get_prime_factors(num)` to find the prime factors of `num`, and `sum_of_primes(num)` to calculate the sum of all prime numbers less than `num`. The `is_prime(num)` function should return `True` if `num` is prime and `False` otherwise. The `get_prime_factors(num)` function should return a list of prime factors of `num`. The `sum_of_primes(num)` function should return the sum of all prime numbers less than `num`. Use these functions to determine whether a given number is prime or not, calculate the sum of all prime numbers less than the given number, and display the prime factors if the number is not prime.
"""

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_prime_factors(num):
    """Get the prime factors of a number."""
    factors = []
    for i in range(2, int(num**0.5) + 1):
        while num % i == 0:
            factors.append(i)
            num //= i
    if num > 1:
        factors.append(num)
    return factors

def sum_of_primes(num):
    """Calculate the sum of all prime numbers less than a given number."""
    sum_primes = 0
    for i in range(2, num):
        if is_prime(i):
            sum_primes += i
    return sum_primes