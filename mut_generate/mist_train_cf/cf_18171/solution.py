"""
QUESTION:
Write a function `remove_duplicates_sort_tuples` that takes a list of integer tuples as input, removes exact duplicate tuples, and returns the remaining tuples sorted in descending order based on the sum of their elements. If two tuples have the same sum, they should be sorted based on the product of their elements in ascending order.
"""

import math

def remove_duplicates_sort_tuples(list1):
    # Remove duplicate tuples
    unique_tuples = list(set(list1))

    # Sort the remaining tuples
    sorted_tuples = sorted(unique_tuples, key=lambda x: (-sum(x), math.prod(x)))

    return sorted_tuples