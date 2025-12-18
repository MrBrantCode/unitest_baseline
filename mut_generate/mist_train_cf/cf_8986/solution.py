"""
QUESTION:
Write a function named `intersection` that takes two sorted lists as input and returns their intersection. The intersection should be a list containing only unique elements, sorted in ascending order, and without duplicates.
"""

def intersection(list1, list2):
    """
    This function takes two sorted lists as input and returns their intersection.
    The intersection is a list containing only unique elements, sorted in ascending order, and without duplicates.

    Args:
        list1 (list): The first sorted list.
        list2 (list): The second sorted list.

    Returns:
        list: The intersection of list1 and list2.
    """
    result = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            i += 1
        elif list1[i] > list2[j]:
            j += 1
        else:
            if list1[i] not in result:
                result.append(list1[i])
            i += 1
            j += 1

    return result