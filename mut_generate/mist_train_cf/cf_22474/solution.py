"""
QUESTION:
Create a function called merge_lists that merges two sorted lists, list1 and list2, by alternating elements, removes any duplicates, and returns the merged list in ascending order. The function should handle lists of different lengths and should not use any built-in sorting functions.
"""

def merge_lists(list1, list2):
    """
    Merges two sorted lists, list1 and list2, by alternating elements, removes any duplicates, 
    and returns the merged list in ascending order.

    Args:
    list1 (list): The first sorted list.
    list2 (list): The second sorted list.

    Returns:
    list: The merged list in ascending order with no duplicates.
    """
    merged_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1
            j += 1

    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    # Remove duplicates by only keeping elements that are different from the previous one
    unique_list = []
    for i in range(len(merged_list)):
        if i == 0 or merged_list[i] != merged_list[i - 1]:
            unique_list.append(merged_list[i])

    return unique_list