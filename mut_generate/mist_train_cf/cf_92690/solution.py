"""
QUESTION:
Create a function named `is_prime(n)` that returns a boolean indicating whether a given number `n` is prime or not, and use it to generate an array of the first 100 unique prime numbers in the range 1 to 1000.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True