"""
QUESTION:
Write a function `is_prime()` that checks if a number `n` is prime using a recursive approach, and then use this function to generate a string of prime numbers from 1 to 500, where each prime number is preceded by "Prime " and followed by a comma and a space.
"""

def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)