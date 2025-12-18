"""
QUESTION:
Design a function `find_intersection(list_one, list_two)` that takes two lists of integers as input and returns a list of integers representing the intersection of the two input lists. The intersection should contain the common elements in the order they appear in `list_one`. Assume that the input lists do not contain any duplicate elements. Do not use any built-in intersection functions or sets.
"""

def find_intersection(list_one, list_two):
    """
    This function takes two lists of integers as input and returns a list of integers representing the intersection of the two input lists.
    
    The intersection contains the common elements in the order they appear in `list_one`. 
    It is assumed that the input lists do not contain any duplicate elements.
    
    :param list_one: The first list of integers
    :param list_two: The second list of integers
    :return: A list of integers representing the intersection of the two input lists
    """
    intersection = []
    for num in list_one:
        if num in list_two:
            intersection.append(num)
    return intersection