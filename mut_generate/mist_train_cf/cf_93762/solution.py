"""
QUESTION:
Create a function called `distinct_permutations` that takes a string as input and returns a list of distinct permutations of the string in lexicographical order, with no duplicates, even if the input string contains duplicate characters.
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