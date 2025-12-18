"""
QUESTION:
Implement the `is_prime` function to determine whether a given positive integer is a prime number, returning `True` if the number is prime and `False` otherwise. The function should efficiently handle large input values without using external libraries or built-in prime-checking functions.
"""

def is_prime(n):
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