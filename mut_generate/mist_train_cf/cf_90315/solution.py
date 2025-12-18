"""
QUESTION:
Write a function `is_prime(n)` that takes an integer `n` as input and returns a boolean indicating whether `n` is a prime number. Use this function to output all prime numbers between 1 and 10,000.
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