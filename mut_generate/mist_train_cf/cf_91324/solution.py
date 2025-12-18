"""
QUESTION:
Create a function called `add_sets` that merges two lists of numbers and returns the merged list in ascending order. The input lists may not be sorted. The function should take two lists of numbers as input parameters and return a single sorted list containing all numbers from both input lists.
"""

def add_sets(set1, set2):
    merged_set = sorted(set1 + set2)
    return merged_set