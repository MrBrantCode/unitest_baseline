"""
QUESTION:
Write a function `is_prime` to check if a number is prime and use it to find the 100th prime number greater than 1000. The function `is_prime(n)` should return `True` if the number `n` is prime and `False` otherwise.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True