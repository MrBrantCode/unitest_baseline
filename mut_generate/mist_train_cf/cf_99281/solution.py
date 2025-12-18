"""
QUESTION:
Create a function `is_prime(n)` that determines if a number `n` is prime. Use this function in a loop that starts from 2 and identifies the first 10 prime numbers, then calculate their sum. The loop should only stop once 10 prime numbers have been found. Ensure that the `is_prime(n)` function checks for primality correctly.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True