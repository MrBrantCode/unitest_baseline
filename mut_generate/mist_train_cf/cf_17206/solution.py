"""
QUESTION:
Write a function `filter_primes` that takes a list of integers as input, removes duplicates, sorts the resulting set in ascending order, and returns only the prime numbers. The function should be implemented in a single line of code.
"""

def filter_primes(lst):
    return sorted(set(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5)+1)) and x != 1, lst)))