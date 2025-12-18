"""
QUESTION:
Write a function named `isPrime` that takes an integer `n` as input and returns a boolean value indicating whether `n` is a prime number. The function should return `True` if `n` is a prime number and `False` otherwise.
"""

def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6
    return True