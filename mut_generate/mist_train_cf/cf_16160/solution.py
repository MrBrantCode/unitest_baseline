"""
QUESTION:
Write a function `get_unique_elements(lst)` that takes in a list `lst` containing elements of any type and returns a new list containing only the unique elements from the original list, preserving their original order. The function should also remove any duplicates within the original list, so that the modified original list only contains the unique elements. The function must optimize its algorithm for finding unique elements, handle lists with millions of elements efficiently, and run in linear time complexity (O(n)) with respect to the input size.
"""

def get_unique_elements(lst):
    """
    Returns a new list containing only the unique elements from the original list, 
    preserving their original order. The function also removes any duplicates within 
    the original list, so that the modified original list only contains the unique 
    elements.

    This function optimizes its algorithm for finding unique elements, handles lists 
    with millions of elements efficiently, and runs in linear time complexity (O(n)) 
    with respect to the input size.

    Args:
        lst (list): A list containing elements of any type.

    Returns:
        list: A new list containing only the unique elements from the original list.
    """
    unique_set = set()
    unique_list = []
    for elem in lst:
        if elem not in unique_set:
            unique_set.add(elem)
            unique_list.append(elem)
    return unique_list