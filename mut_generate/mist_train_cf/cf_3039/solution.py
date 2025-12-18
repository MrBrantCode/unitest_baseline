"""
QUESTION:
Write a function `prime_subsets` that returns a list of all possible subsets of the given list that have a sum greater than 5 and contain only prime numbers. The function should use list comprehension and return a list of tuples, where each tuple is a subset of the given list.
"""

from itertools import chain, combinations

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_subsets(lst):
    subsets = list(chain(*map(lambda x: combinations(lst, x), range(0, len(lst) + 1))))
    return [subset for subset in subsets if sum(subset) > 5 and all(is_prime(num) for num in subset)]