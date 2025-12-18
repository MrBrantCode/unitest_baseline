"""
QUESTION:
Create a function `find_prime_permutations(num)` that takes a positive integer `num` as input and returns a list of all prime numbers that can be formed by permuting its digits. The function should have a time complexity of O(n!), where n is the number of digits in the input number, and should not significantly increase the time complexity compared to the original function.
"""

from itertools import permutations
from math import sqrt

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_permutations(num):
    num_str = str(num)
    digits = [int(d) for d in num_str]
    prime_permutations = set()
    for perm in permutations(digits):
        num_perm = int("".join(map(str, perm)))
        if is_prime(num_perm):
            prime_permutations.add(num_perm)
    return list(prime_permutations)