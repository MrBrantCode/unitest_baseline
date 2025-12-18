"""
QUESTION:
Write a function `is_prime(n)` that checks if a given number `n` is prime or not and use it to calculate the sum of all prime numbers between 1 and 100000. The function should return `True` if `n` is prime and `False` otherwise. Note that the range is inclusive and the function should be efficient enough to handle large numbers.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True