"""
QUESTION:
Write a function named `analyze_numbers` that takes a list of numeric values as input and returns a dictionary mapping each distinct element to its frequency of occurrence and a list of tuples. Each tuple should contain a distinct number and a list of its indices in the order of their appearance. The function should have a time complexity of O(n).
"""

from collections import defaultdict

def entance(nums):
    num_freqs = defaultdict(int)
    num_indices = {}

    for i, num in enumerate(nums):
        num_freqs[num] += 1
        if num not in num_indices:
            num_indices[num] = [i]
        else:
            num_indices[num].append(i)

    num_indices_list = list(num_indices.items())

    return num_freqs, num_indices_list