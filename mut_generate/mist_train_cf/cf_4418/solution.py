"""
QUESTION:
Function: generate_permutations
Input: A list of integers
Restriction: The function should return all unique permutations of exactly 5 numbers from the input list, with exactly 3 odd numbers and 2 even numbers.
"""

from itertools import permutations

def generate_permutations(nums):
    """
    Generates all unique permutations of exactly 5 numbers from the input list, 
    with exactly 3 odd numbers and 2 even numbers.

    Args:
    nums (list): A list of integers.

    Returns:
    list: A list of lists, where each sublist is a permutation of 5 numbers from the input list.
    """
    # Separate odd and even numbers
    odd_nums = [num for num in nums if num % 2 != 0]
    even_nums = [num for num in nums if num % 2 == 0]

    # Generate permutations
    perms = []
    for perm in permutations(nums, 5):
        # Check if the permutation has exactly 3 odd numbers and 2 even numbers
        if len([num for num in perm if num in odd_nums]) == 3 and len([num for num in perm if num in even_nums]) == 2:
            perms.append(list(perm))

    # Remove duplicates by converting to a set of tuples and then back to a list of lists
    perms = [list(t) for t in set(tuple(sorted(perm)) for perm in perms)]

    return perms