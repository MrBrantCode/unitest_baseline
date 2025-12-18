"""
QUESTION:
Write a function `is_prime(n)` that determines whether a given positive integer `n` is prime or not. The function should have a time complexity of O(sqrt(n)) and should not use any built-in functions or libraries. The function should return `True` if the number is prime and `False` otherwise.
"""

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True