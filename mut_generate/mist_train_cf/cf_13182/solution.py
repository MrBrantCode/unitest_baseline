"""
QUESTION:
Create a function named `is_prime(n)` to check if a number is prime, then use this function to generate a list of 100 unique prime numbers from 1 to 1000.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True