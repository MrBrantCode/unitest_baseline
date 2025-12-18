"""
QUESTION:
Write a function `findCombinations` that takes a list of positive integers as input and returns all unique combinations of two or more numbers whose product is a perfect square. The function should be able to handle larger datasets efficiently.
"""

from collections import Counter
from math import prod
from itertools import combinations

def primefactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def isPerfectSquare(n):
    factors_map = Counter(primefactors(n))
    return all(v % 2 == 0 for v in factors_map.values())

def findCombinations(lst):
    res = []
    for r in range(2, len(lst)+1):
        for comb in combinations(lst, r):
            if isPerfectSquare(prod(comb)):
                res.append(list(comb))
    return res