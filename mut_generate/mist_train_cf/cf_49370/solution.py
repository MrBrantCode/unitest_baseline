"""
QUESTION:
Given a list of numbers, an integer k, and an integer n between 1 and the length of the list, create a function `check_sum(nums, k, n)` that returns True if any n numbers from the list add up to k, and False otherwise. Assume the list can contain any real number, including negatives and fractions. The function should be able to handle a large number of elements within the list efficiently.
"""

import itertools

def entrance(nums, k, n):
    return any(sum(subset) == k for subset in itertools.combinations(nums, n))