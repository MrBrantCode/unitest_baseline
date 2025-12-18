"""
QUESTION:
Create a function called `merge_sorted_lists` that takes two sorted lists of integers, `list_1` and `list_2`, as input and returns a new sorted list containing all elements from both lists in descending order. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the total number of elements in `list_1` and `list_2`. The function should use a single while loop and no additional data structures except for the result list.
"""

def merge_sorted_lists(list_1, list_2):
    """
    Merge two sorted lists into a new sorted list in descending order.

    Args:
        list_1 (list): The first sorted list of integers.
        list_2 (list): The second sorted list of integers.

    Returns:
        list: A new sorted list containing all elements from both lists in descending order.
    """
    merged_list = []
    i = len(list_1) - 1
    j = len(list_2) - 1
    
    while i >= 0 and j >= 0:
        if list_1[i] > list_2[j]:
            merged_list.append(list_1[i])
            i -= 1
        else:
            merged_list.append(list_2[j])
            j -= 1
    
    while i >= 0:
        merged_list.append(list_1[i])
        i -= 1
    
    while j >= 0:
        merged_list.append(list_2[j])
        j -= 1
    
    return merged_list