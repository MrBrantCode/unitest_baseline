"""
QUESTION:
Write a function called "find_intersection" that takes two sets A and B as input, and returns their intersection. The function should be able to handle sets with up to 10,000 elements. 

Note: The function should only return the intersection set, without printing it.
"""

def find_intersection(A, B):
    """
    This function finds the intersection of two sets A and B.

    Args:
        A (set): The first set.
        B (set): The second set.

    Returns:
        set: The intersection of sets A and B.
    """
    intersection_set = set() 
    for element in A: 
        if element in B: 
            intersection_set.add(element) 
    return intersection_set