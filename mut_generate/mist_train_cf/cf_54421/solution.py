"""
QUESTION:
Create a function `is_prime(n)` that takes an integer `n` as input and returns `True` if it's a prime number (with exactly two distinct positive divisors) and `False` otherwise, without using any built-in primality tests or number theory libraries. The function should be efficient and able to handle large numbers, and it should only check divisibility up to the square root of the given number.
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