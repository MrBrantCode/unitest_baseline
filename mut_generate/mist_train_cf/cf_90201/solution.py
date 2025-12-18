"""
QUESTION:
Write a function named `is_prime` that checks whether a given number is prime and use it to print all prime numbers between 1 and 100 in ascending order. The function should take an integer `n` as input and return a boolean value.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True