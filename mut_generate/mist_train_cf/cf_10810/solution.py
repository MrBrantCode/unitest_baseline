"""
QUESTION:
Create a function named `is_prime(num)` to determine if a given number is prime, and use it to print all prime numbers from 0 to 100. The function should return `True` if the number is prime and `False` otherwise.
"""

def entrance(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True