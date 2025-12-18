"""
QUESTION:
Write a function named `is_prime` that determines if a given number is prime or not. Using this function, calculate the sum of the first 100 prime numbers and return the result.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True