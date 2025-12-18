"""
QUESTION:
Create a function named `is_prime` that checks whether a given integer is prime or not. The function should not use any built-in functions or libraries. Using the `is_prime` function, print the prime numbers between 0 and 100 in descending order with a single loop.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True