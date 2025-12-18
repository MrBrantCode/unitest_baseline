"""
QUESTION:
Write a function `find_intersection(list1, list2)` to find the intersection of two sorted lists, `list1` and `list2`. The function should return a sorted list containing unique elements common to both input lists, excluding duplicates. The input lists may contain duplicate elements, but the output should not.
"""

def find_intersection(list1, list2):
    """
    This function finds the intersection of two sorted lists, excluding duplicates.

    Args:
        list1 (list): The first sorted list.
        list2 (list): The second sorted list.

    Returns:
        list: A sorted list containing unique elements common to both input lists.
    """
    intersection = []
    i = 0
    j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            if list1[i] not in intersection:
                intersection.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    
    return intersection