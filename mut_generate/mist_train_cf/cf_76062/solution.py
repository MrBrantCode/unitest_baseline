"""
QUESTION:
Write a function named `is_prime` that takes an integer `n` as input, checks if `n` is a prime number, and returns a boolean value. Use this function to create a loop that prints all prime numbers between 0 and 25 that are situated at prime indexes. A prime number is a number that has exactly two distinct positive divisors: 1 and itself, and an index is considered to be at a prime position if it is a prime number.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True