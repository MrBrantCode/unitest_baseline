"""
QUESTION:
Create a function named `is_prime(n)` to check if a given number `n` is prime. The function should return `True` if `n` is prime and `False` otherwise. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should be able to handle numbers within the range of 20 to 80.
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