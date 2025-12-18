"""
QUESTION:
Create a function `divisible_by_primes(n)` that takes a positive integer `n` as input and returns a list of boolean values representing whether `n` is divisible by each prime number from 2 to 19. The list should contain boolean responses in the order of the prime numbers 2, 3, 5, 7, 11, 13, 17, and 19, where `True` indicates `n` is divisible by the prime and `False` otherwise.
"""

def divisible_by_primes(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    return [n % prime == 0 for prime in primes]