"""
QUESTION:
Write a function `symmetric_difference(set1, set2)` that takes two sets as input and returns a new set containing the symmetric difference of the input sets. The symmetric difference of two sets A and B is the set of elements that are in either A or B, but not in both. Implement this function with a time complexity of O(n), where n is the total number of elements in both input sets.
"""

def symmetric_difference(set1, set2):
    """
    This function calculates the symmetric difference of two sets.
    
    Args:
        set1 (set): The first set.
        set2 (set): The second set.
    
    Returns:
        set: A new set containing the symmetric difference of the input sets.
    """
    return {x for x in set1 ^ set2}