"""
QUESTION:
Write a function `is_disjoint` that checks if two sets are disjoint. Two sets are disjoint if they have no elements in common. The function should take two sets as input and return a boolean value indicating whether the sets are disjoint or not.
"""

def is_disjoint(set1, set2):
    """
    Checks if two sets are disjoint.

    Args:
        set1 (set): The first set.
        set2 (set): The second set.

    Returns:
        bool: True if the sets are disjoint, False otherwise.
    """
    return len(set1.intersection(set2)) == 0