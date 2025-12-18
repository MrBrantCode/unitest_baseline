"""
QUESTION:
Construct a function named `prime_pairs` that takes a list of integers as input. The function should return three values: the total count of unordered pairs with non-identical elements, the count of pairs where the difference forms a prime number, and a list of those pairs. The function should be computationally efficient for large lists and handle edge cases such as empty lists or lists with only one element.
"""

import itertools
import math

def prime_pairs(int_list):
    if len(int_list) < 2:
        return 0, 0, []
    
    int_set = set(int_list)
    
    if len(int_set) == 1:
        return 0, 0, []
    
    pairs = list(itertools.combinations(int_set, 2))

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, math.isqrt(num) + 1):
            if num % i == 0:
                return False
        return True
    
    prime_pairs = [(i, j) for i, j in pairs if is_prime(abs(i -j))]

    return len(pairs), len(prime_pairs), prime_pairs