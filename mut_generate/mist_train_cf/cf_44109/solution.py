"""
QUESTION:
Create a function named `find_sequence(arr)` that takes a list of integers as input and returns a sequence of integers from the list such that the sum of any two neighboring elements is a prime number. The function should return `None` if no such sequence exists.
"""

import itertools

def is_prime(n):
    """Checks if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_sequence(arr):
    """Finds a sequence where the sum of neighbors is a prime number"""
    for perm in itertools.permutations(arr):
        if all(is_prime(perm[i] + perm[i+1]) for i in range(len(perm) - 1)):
            return perm
    return None