"""
QUESTION:
Construct a generator expression using a function named `is_prime` to traverse a given array of integers and yield exclusively the prime numbers. The `is_prime` function should take one integer as an argument and return a boolean indicating whether the number is prime or not.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True