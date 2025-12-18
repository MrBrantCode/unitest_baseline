"""
QUESTION:
Design a function to generate a permutation sequence from a given array such that the sum of any consecutive pair of numbers in the sequence results in a prime number. The function should take an array of integers as input and return a permutation sequence if one exists, or indicate that no such permutation exists. The array [3, 1, 4, 2] should be used as the input array.
"""

import itertools

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all([(n % i) for i in range(3, int(n**0.5) + 1, 2)])

def permute_to_prime_pairs(arr):
    permutations = list(itertools.permutations(arr))
    for perm in permutations:
        if all(is_prime(perm[i] + perm[i+1]) for i in range(len(perm)-1)):
            return perm
    return None