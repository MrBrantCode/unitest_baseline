"""
QUESTION:
Write a function `find_permutations(str1, str2, limit)` that finds all unique permutations of letters from two given strings `str1` and `str2`, where the order of the characters matters. The combined length of two strings for each permutation should not exceed the specified `limit`, and each combination should contain at least one character from each string.
"""

from itertools import permutations

def find_permutations(str1, str2, limit):
    combined = str1 + str2
    all_perms = []
    for i in range(2, limit+1):
        all_perms.extend(permutations(combined, i))
    results = []
    for perm in all_perms:
        perm_str = ''.join(perm)
        if any(char in perm_str for char in str1) and any(char in perm_str for char in str2):
            results.append(perm_str)
    return list(set(results))