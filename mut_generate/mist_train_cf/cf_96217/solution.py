"""
QUESTION:
Create a function named `is_prime(n)` that checks whether a given number `n` is prime or not. This function should return `True` if the number is prime, `False` otherwise. Use this function to print all prime numbers in the range 0 to 100,000.
"""

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True