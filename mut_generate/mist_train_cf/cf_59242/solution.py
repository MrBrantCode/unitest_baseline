"""
QUESTION:
Write a function `solve_problem(lst)` that takes a list of numbers as input, replaces the prime numbers in the list with their factorials, and returns the updated list sorted in descending order. The function should only calculate the factorial for prime numbers and leave composite numbers unchanged.
"""

from math import factorial

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def solve_problem(lst):
    return sorted((factorial(x) if is_prime(x) else x for x in lst), reverse=True)