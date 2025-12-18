"""
QUESTION:
Write a function, `is_prime`, that takes an integer as input and returns `True` if the number is prime and `False` otherwise. Then, using this function, print all prime numbers between 1000 and 2000 (inclusive) that do not contain the digit 5.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True