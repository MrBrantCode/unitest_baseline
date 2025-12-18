"""
QUESTION:
Create a function named `generate_prime_sequence` that takes an integer `n` as input and returns a list of prime numbers less than or equal to `n`. The function should use a helper function `is_prime` to check if a number is prime. The `is_prime` function should check for primality up to the square root of the number.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_div = int(n**0.5) + 1
    for div in range(3, max_div, 2):
        if n % div == 0:
            return False
    return True

def generate_prime_sequence(n):
    primes = []
    for possible_prime in range(2, n + 1):
        if is_prime(possible_prime):
            primes.append(possible_prime)
    return primes