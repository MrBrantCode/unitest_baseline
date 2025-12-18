"""
QUESTION:
Write a function named `find_prime_indices` that takes a list of integers as input, identifies the prime numbers in the list, and returns their indices. The function should be efficient enough to handle large lists. The input list may contain duplicate values and may not be sorted.
"""

def find_prime_indices(lst):
    is_prime = lambda x: all([(x%j) for j in range(2, int(x**0.5) + 1)]) and x >= 2
    return [i for i, x in enumerate(lst) if is_prime(x)]