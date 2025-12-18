"""
QUESTION:
Write a function called `merge_lists` that takes two sorted lists `list1` and `list2` as input, merges them into one sorted list, and returns the merged list in descending order. The function should not use the `sort()` method or any built-in sorting function. It should implement a sorting algorithm with a time complexity of O(n log n) or better.
"""

def merge_lists(list1, list2):
    """
    Merge two sorted lists into one sorted list in descending order.

    Args:
        list1 (list): The first sorted list.
        list2 (list): The second sorted list.

    Returns:
        list: The merged sorted list in descending order.
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