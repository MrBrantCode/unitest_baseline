"""
QUESTION:
Write a function called `is_prime` and use it to find the sum of all prime numbers from 1 to 1000. The function `is_prime(n)` should return True if a number `n` is prime and False otherwise.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True