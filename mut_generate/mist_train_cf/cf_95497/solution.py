"""
QUESTION:
Write a function `is_prime` that takes an integer `n` as input and returns `True` if the number is prime and `False` otherwise. The function should not use any built-in functions or libraries to check if a number is prime. Instead, it should use a manual algorithm to determine if a number is prime. 

The function will be used to filter prime numbers from a list of integers. Implement the `is_prime` function and use it to generate a new list containing only the prime numbers from the original list.
"""

def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True