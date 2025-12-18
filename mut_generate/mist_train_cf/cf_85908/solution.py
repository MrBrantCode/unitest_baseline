"""
QUESTION:
Write a function `find_triplets(nums, threshold)` that identifies all unique combinations of three elements within an array `nums` that, when multiplied together, exceed a specified `threshold` value. The function should accept an array of integers and an integer threshold as input, and return a list of lists where each sublist is a qualifying triplet. If the array has fewer than three elements, return a message indicating insufficient quantity of numbers.
"""

from itertools import combinations

def find_triplets(nums, threshold):
    if len(nums) < 3:
        return "Input array has insufficient quantity of numbers."
    else:
        triplets = list(combinations(nums, 3))
        result = [list(triplet) for triplet in triplets if triplet[0] * triplet[1] * triplet[2] > threshold]
        return result