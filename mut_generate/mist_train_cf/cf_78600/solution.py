"""
QUESTION:
Write a function called `find_intersection` that takes two lists of integers as input and returns their intersection without using built-in intersection functions. The function should also remove any duplicate values from the intersection. Assume the input lists do not contain duplicate values.
"""

def find_intersection(list1, list2):
    """
    Find the intersection of two lists without duplicates.
    
    Parameters:
    list1 (list): The first list of integers.
    list2 (list): The second list of integers.
    
    Returns:
    list: A list of integers that are common to both input lists, without duplicates.
    """
    intersection = []
    for i in list1:
        if i in list2 and i not in intersection:
            intersection.append(i)
    return intersection