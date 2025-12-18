"""
QUESTION:
Write a function called `generate_arithmetic_combinations` that takes no arguments. The function should generate all distinct combinations of 5 prime numbers between 2 and 20 in ascending order, check each combination to see if it forms an arithmetic progression, and return a list of all combinations that are arithmetic progressions.
"""

from itertools import combinations
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_arithmetic(lst):
    diff = lst[1] - lst[0]
    for index in range(len(lst) - 1):
        if not (lst[index + 1] - lst[index] == diff):
             return False
    return True

def generate_arithmetic_combinations():
    primes = sorted([i for i in range(2, 21) if is_prime(i)])
    combs = list(combinations(primes, 5))
    return [comb for comb in combs if is_arithmetic(comb)]