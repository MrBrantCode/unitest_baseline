"""
QUESTION:
Create a function `is_prime(n)` that determines if a number is prime and use it to print all prime numbers between 1 and 20. The function should take an integer `n` as input and return `True` if it's prime and `False` otherwise. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True