"""
QUESTION:
Write a function named `solution` that takes a non-empty list of whole numbers as input and returns the sum of square roots of all prime numbers located at odd indices. The function should be efficient enough to handle large inputs of up to 10^6 elements.
"""

import math

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def solution(lst):
    return sum(math.sqrt(n) for i, n in enumerate(lst) if i % 2 == 1 and is_prime(n))