"""
QUESTION:
Write a function named `is_prime` to check if a given number is prime or not. The function should take an integer as input and return `True` if it is prime, `False` otherwise. Use this function to find and print the first 10 prime numbers.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True