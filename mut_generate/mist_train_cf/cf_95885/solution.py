"""
QUESTION:
Create a function called `is_permutation_prime` that takes an integer `num` as input and returns `True` if any permutation of its digits is a prime number, and `False` otherwise. The function should consider all possible permutations of the digits in `num`, and check each permutation for primality.
"""

import itertools

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_permutation_prime(num):
    num_str = str(num)
    permutations = list(itertools.permutations(num_str))
    for perm in permutations:
        perm_num = int(''.join(perm))
        if is_prime(perm_num):
            return True
    return False