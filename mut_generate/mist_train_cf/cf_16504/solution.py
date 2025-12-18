"""
QUESTION:
Write a function `is_prime` that checks if a number `n` is prime and use it to calculate the sum of the first 1000 prime numbers. The function should only take an integer as input and return a boolean value indicating whether the number is prime or not. The sum should be calculated by iterating through numbers starting from 2.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True