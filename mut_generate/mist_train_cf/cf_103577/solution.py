"""
QUESTION:
Create a function named symmetric_difference_count that takes two sets of integers as input and returns the count of distinct elements in their symmetric difference. Each set should have between 5 and 10 elements, and all elements should be positive integers between 1 and 1000.
"""

def symmetric_difference_count(set1, set2):
    """
    Calculate the count of distinct elements in the symmetric difference of two sets.

    Args:
        set1 (set): The first set of integers.
        set2 (set): The second set of integers.

    Returns:
        int: The count of distinct elements in the symmetric difference of set1 and set2.
    """
    symmetric_difference = set1.symmetric_difference(set2)
    return len(symmetric_difference)