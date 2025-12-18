"""
QUESTION:
Create a function named `symmetric_difference` that takes two sets as input and returns their symmetric difference. The symmetric difference of two sets A and B is a set of elements which are in either of the sets, but not in their intersection.
"""

def symmetric_difference(set1, set2):
    """
    Returns the symmetric difference of two sets.
    
    Args:
        set1 (set): The first set.
        set2 (set): The second set.
    
    Returns:
        set: The symmetric difference of set1 and set2.
    """
    return set1.symmetric_difference(set2)