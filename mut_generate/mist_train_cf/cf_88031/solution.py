"""
QUESTION:
Create a function `is_prime()` and use it to generate a list of the first 100 prime numbers, including both odd and even primes, and return the list in descending order. The list should contain exactly 100 prime numbers.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True