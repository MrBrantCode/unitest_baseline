"""
QUESTION:
Create a function named `is_prime(n)` that checks whether a given number `n` is prime or not. Then, using list comprehension, generate a list of all prime numbers between 1 and 1000, and calculate the sum and product of these prime numbers. The `is_prime(n)` function should be able to handle any positive integer `n`.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True