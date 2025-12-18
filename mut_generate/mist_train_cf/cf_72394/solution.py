"""
QUESTION:
Create a function called `merge_lists` that merges two sorted lists, `list1` and `list2`, into a new sorted list without using built-in sort functions. The function should maintain the original ascending order of the elements within each list and return the merged list. The input lists are guaranteed to be sorted in ascending order.
"""

def merge_lists(list1, list2):
    """
    Merge two sorted lists into a new sorted list without using built-in sort functions.
    
    Args:
    list1 (list): The first sorted list.
    list2 (list): The second sorted list.
    
    Returns:
    list: A new sorted list containing all elements from both input lists.
    """
    res = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1
    # add remaining elements
    res.extend(list1[i:])
    res.extend(list2[j:])
    return res