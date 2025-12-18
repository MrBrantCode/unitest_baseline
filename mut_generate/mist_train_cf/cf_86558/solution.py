"""
QUESTION:
Implement the function `merge_lists(list1, list2)` that merges two sorted lists `list1` and `list2` into one sorted list in descending order without using the `sort()` method or any built-in sorting function. The function should have a time complexity of O(n log n) or better. 

Note that both input lists `list1` and `list2` are already sorted.
"""

def merge_lists(list1, list2):
    """
    Merges two sorted lists into one sorted list in descending order.

    Args:
        list1 (list): The first sorted list.
        list2 (list): The second sorted list.

    Returns:
        list: A new sorted list containing all elements from list1 and list2 in descending order.
    """
    merged_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] >= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list