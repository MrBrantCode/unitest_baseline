"""
QUESTION:
Write a function `permute` that takes a list of integers as input and returns all unique permutations of three elements from the list, considering the possibility of duplicate numbers. The function should not include any duplicate permutations in its output.
"""

from itertools import permutations

def permute(nums):
    unique_perms = set(permutations(nums, 3))  
    return [list(perm) for perm in unique_perms]