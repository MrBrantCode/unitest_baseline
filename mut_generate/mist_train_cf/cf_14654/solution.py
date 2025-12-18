"""
QUESTION:
Write a function called `sorted_intersection` that takes two sets as input and returns a list of their intersection in descending order, with no duplicates.
"""

def sorted_intersection(set1, set2):
    """
    Returns a list of the intersection of two sets in descending order, with no duplicates.
    
    Parameters:
    set1 (set): The first set.
    set2 (set): The second set.
    
    Returns:
    list: A list of the intersection of set1 and set2 in descending order, with no duplicates.
    """
    intersection_set = set.intersection(set1, set2)
    return sorted(intersection_set, reverse=True)