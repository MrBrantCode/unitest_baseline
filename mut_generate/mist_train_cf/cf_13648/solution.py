"""
QUESTION:
Create a function `is_prime(n)` that takes an integer `n` as input and returns `True` if the number is prime, and `False` otherwise. Then, using this function, iterate through a given list of integers and print all the prime numbers. The function should be efficient and handle large numbers.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True