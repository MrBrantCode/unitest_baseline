"""
QUESTION:
Design a function `compare_lists(list_one, list_two)` that compares two sorted lists and returns a list of common elements and a list of their indices in both input lists. The function should count common elements multiple times based on their occurrences in both lists.
"""

def compare_lists(list_one, list_two):
    """
    Compare two sorted lists and return a list of common elements and a list of their indices in both input lists.
    
    Args:
        list_one (list): The first sorted list.
        list_two (list): The second sorted list.
    
    Returns:
        tuple: A tuple containing a list of common elements and a list of their indices in both input lists.
    """
    common_elements = []
    indices = []
    i = 0
    j = 0
    
    while i < len(list_one) and j < len(list_two):
        if list_one[i] == list_two[j]:
            common_elements.append(list_one[i])
            indices.append((i, j))
            i += 1
            j += 1
        elif list_one[i] < list_two[j]:
            i += 1
        else:
            j += 1
    
    return common_elements, indices