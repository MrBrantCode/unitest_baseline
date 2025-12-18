"""
QUESTION:
Write a Python function named `is_prime` to check if a number is prime, and another function `main` to calculate the sum of all prime numbers from 1 to 100. The `is_prime` function should take an integer as input and return a boolean value, and the `main` function should print the sum of prime numbers. The `is_prime` function should check for factors up to half of the input number.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False
    return True