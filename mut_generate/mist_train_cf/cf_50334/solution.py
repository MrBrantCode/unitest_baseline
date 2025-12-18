"""
QUESTION:
Write a function named `is_prime(n)` to determine whether a given integer `n` is a prime number or not. The function should take an integer as input and return `True` if the number is prime, and `False` otherwise. The function should work for integers within the range 1 to 10, excluding both endpoints.
"""

def entrance(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while(i * i <= n):
        if(n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True