"""
QUESTION:
Create a function called `is_prime(n)` that takes an integer `n` as input and returns `True` if it's a prime number, and `False` otherwise. The function should be able to identify prime numbers within a specific range, excluding the endpoints. Use this function to find all prime numbers between 2 and 9 (exclusive).
"""

def entrance(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True