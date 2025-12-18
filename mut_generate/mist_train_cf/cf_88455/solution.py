"""
QUESTION:
Write a function named `is_prime(n)` that checks if a number `n` is prime or not without using built-in functions or libraries. Implement a main loop that prints out the prime numbers between 0 and 100 in descending order using a single loop. The loop should start from 100 and go down to 2, checking for primality using the `is_prime(n)` function.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True