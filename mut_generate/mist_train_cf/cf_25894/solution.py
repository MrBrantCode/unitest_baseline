"""
QUESTION:
Write a function `combinations(n, k)` to calculate the number of unique combinations of k items from a set of n items (0 to n-1). The function should take two parameters, `n` and `k`, where `n` is the total number of items and `k` is the number of items to choose from the set.
"""

from math import factorial

def combinations(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))