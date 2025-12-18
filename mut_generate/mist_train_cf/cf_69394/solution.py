"""
QUESTION:
Write a function named `min_disparity` that calculates the minimum absolute difference between a target value and all possible permutations of a given list of numbers. The function should return the minimum absolute difference and the corresponding arrangement of numbers. The input parameters are a target value and a list of numbers. Assume the list of numbers is non-empty and contains only integers.
"""

from itertools import permutations

def min_disparity(target, num_array):
    min_diff = float('inf')
    for p in permutations(num_array):
        sum_of_elements = sum(p)
        diff = abs(target - sum_of_elements)
        if diff < min_diff:
            min_diff = diff
            best_p = p
    return min_diff, best_p