"""
QUESTION:
Write a function named `is_prime(n)` and use it to print the multiplication tables for all prime numbers from 1 to 20. The multiplication tables should be displayed for numbers 1 through 10.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True