"""
QUESTION:
Write a function named `generate_pairs` to produce all unique pairs of elements from the input list `num_list`, excluding pairs of the same elements, and return the result as a list of tuples. The function should have a time complexity better than O(n^2) and use less memory.
"""

from itertools import combinations

def generate_pairs(num_list):
    """
    Generate all unique pairs of elements from the input list, excluding pairs of the same elements.

    Args:
    num_list (list): A list of elements.

    Returns:
    list: A list of tuples, each containing a unique pair of elements from the input list.
    """
    return list(combinations(num_list, 2))