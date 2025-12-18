"""
QUESTION:
Design a function called `find_common_elements` that compares two sorted lists and returns a list with the common elements and their indices in both lists. The function should not use any built-in functions or libraries for searching or comparing elements. The lists can contain duplicates, and the common elements should be counted multiple times based on their occurrences in both lists.
"""

def find_common_elements(list_one, list_two):
    """
    This function compares two sorted lists and returns a list with the common elements 
    and their indices in both lists. The function does not use any built-in functions 
    or libraries for searching or comparing elements.

    Args:
        list_one (list): The first sorted list.
        list_two (list): The second sorted list.

    Returns:
        tuple: A tuple containing a list of common elements, their indices in list_one, 
        and their indices in list_two.
    """
    common_elements = []
    list_one_indices = []
    list_two_indices = []
    
    i = 0
    j = 0
    
    while i < len(list_one) and j < len(list_two):
        if list_one[i] < list_two[j]:
            i += 1
        elif list_one[i] > list_two[j]:
            j += 1
        else:
            common_elements.append(list_one[i])
            list_one_indices.append(i)
            list_two_indices.append(j)
            i += 1
            j += 1
    
    return common_elements, list_one_indices, list_two_indices