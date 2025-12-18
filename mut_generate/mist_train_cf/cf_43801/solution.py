"""
QUESTION:
Write a function `generate_permutations(n, k)` that generates all possible permutations of `k` numbers from the sequence `[1, n]`, where `1 <= n <= 20` and `1 <= k <= n`.
"""

from itertools import permutations

def generate_permutations(n, k):
    # Generate a list with numbers from 1 to n
    nums = list(range(1, n+1))
    
    # Generate all permutations
    perms = permutations(nums, k)
    
    # Convert permutations to lists and return
    return [list(perm) for perm in perms]