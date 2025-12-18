"""
QUESTION:
Generate all possible combinations of distinct subarrays of length three from the given array and print these combinations. Then, for each combination, generate and print all possible sorted permutations in ascending and descending order, excluding duplicates. The function name should be `subarray(arr)`.
"""

from itertools import combinations, permutations as perm

def subarray(arr):
    # Generate all possible combinations of distinct subarrays of length three
    sublist = list(combinations(arr, 3))

    sub_perm = []
    for val in sublist:
        perm_list = list(perm(val))
        for p in perm_list:
            sub_perm.append(p)
            
    # Remove duplicate values
    sub_perm = list(dict.fromkeys(sub_perm))

    # Sort each subarray in ascending and descending order
    sub_perm.sort()

    return sub_perm