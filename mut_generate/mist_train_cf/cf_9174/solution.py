"""
QUESTION:
Create a function `merge_lists(list1, list2)` that merges two sorted lists into a new sorted list. The function should return a list containing all elements from both input lists in ascending order, with all elements from `list1` coming before any element from `list2` if they have the same value. The function should have a time complexity of O(n + m), where n and m are the lengths of `list1` and `list2`, respectively.
"""

def merge_lists(list1, list2):
    merged_list = []
    i = 0  # index for list1
    j = 0  # index for list2

    # Merge the elements of list1 and list2
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append any remaining elements from list1 or list2
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list