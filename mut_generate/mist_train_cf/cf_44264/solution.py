"""
QUESTION:
Write a function `generate_subsets` that takes a string `s` of length `n` (where `n <= 16`) as input and returns all possible non-empty subsets of characters in the string. The function should run in no more than O(2^n) time complexity. Note that the subsets should be returned as strings and should not contain duplicate characters or subsets, and the characters within each subset should be sorted alphabetically.
"""

def generate_subsets(s):
    n = len(s)
    subsets = set()
    # Generate all subsets for 2^n
    for i in range(1, 2**n):
        subset = [s[j] for j in range(n) if (i & (1 << j))]
        subsets.add(''.join(sorted(subset)))  # sorts the subset and joins to a string
    return subsets