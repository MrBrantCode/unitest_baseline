"""
QUESTION:
Write a function `check_prime_indices` that takes a list of integers as input and returns `True` if every prime index of the list contains a prime number, and `False` otherwise. The function should assume 0-based indexing, and consider only the indices that are prime numbers (2, 3, 5, 7, 11, ...).
"""

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def check_prime_indices(lst):
    prime_idx = [i for i in range(len(lst)) if is_prime(i)]
    for idx in prime_idx:
        if not is_prime(lst[idx]):
            return False
    return True