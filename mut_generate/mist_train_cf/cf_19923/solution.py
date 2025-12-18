"""
QUESTION:
Create a function `is_permutation_prime` that takes an integer as input and returns a boolean indicating whether any permutation of its digits is a prime number.
"""

import itertools

def is_permutation_prime(num):
    num_str = str(num)
    permutations = list(itertools.permutations(num_str))
    for perm in permutations:
        perm_num = int(''.join(perm))
        if perm_num > 1: # 1 is not a prime number
            for i in range(2, int(perm_num**0.5) + 1):
                if perm_num % i == 0:
                    break
            else:
                return True
    return False