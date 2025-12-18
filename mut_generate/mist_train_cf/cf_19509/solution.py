"""
QUESTION:
Write a function `is_prime` that checks if a given number is prime and use it to calculate the sum of all prime numbers up to and including a given limit (1000). The function should return the sum of all prime numbers within the limit.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True