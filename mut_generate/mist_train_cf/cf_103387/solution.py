"""
QUESTION:
Create a function `is_prime(num)` to determine whether a given number is prime or not. The function should take an integer as input and return a boolean value. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True