"""
QUESTION:
Write a function `distinct_permutations(string)` that returns all distinct permutations of the input string in lexicographical order. The function should handle strings with duplicate characters and return only unique permutations.
"""

from itertools import permutations

def distinct_permutations(string):
    # Use set to store distinct permutations
    distinct_perms = set()

    # Generate all permutations
    perms = permutations(string)

    # Check if each permutation is distinct
    for perm in perms:
        # Convert the permutation tuple to a string
        perm_str = ''.join(perm)

        # Add the permutation to the set if it is distinct
        distinct_perms.add(perm_str)

    # Convert the set of distinct permutations to a list
    distinct_perms_list = list(distinct_perms)

    # Sort the list of distinct permutations
    distinct_perms_list.sort()

    return distinct_perms_list