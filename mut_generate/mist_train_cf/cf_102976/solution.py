"""
QUESTION:
Create a function `is_prime(n)` that checks if a given number `n` is prime. The function should return `False` for numbers less than or equal to 1, and it should not consider numbers divisible by 2 or 3 as prime.
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