"""
QUESTION:
Write a function `is_prime(num)` that takes an integer as input and returns `True` if the number is prime, `False` otherwise. Using this function, write a loop to print all prime numbers between 1 and 1000 (inclusive). The loop should only print prime numbers.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True