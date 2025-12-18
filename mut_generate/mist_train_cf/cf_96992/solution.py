"""
QUESTION:
Write a function called `is_prime` that determines whether a given number is prime or not and use it to print all prime numbers from 0 to 100. The function should return True for prime numbers and False otherwise.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True