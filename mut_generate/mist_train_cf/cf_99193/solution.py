"""
QUESTION:
Write a function named `intersection` that takes two sets of unique items as arguments and returns a list containing the items that appear in both sets, in the order they appear in the first set.
"""

def intersection(set1, set2):
    """
    Return a list containing the intersection of two sets, in the order they appear in the first set.
    
    Arguments:
    set1 -- a set of unique items
    set2 -- another set of unique items
    
    Returns:
    A list containing the items that appear in both sets, in the order they appear in the first set.
    """
    # Find the common items between the two sets
    common_items = set1.intersection(set2)
    
    # Create a list containing the common items in the order they appear in the first set
    intersection_list = [item for item in set1 if item in common_items]
    
    return intersection_list