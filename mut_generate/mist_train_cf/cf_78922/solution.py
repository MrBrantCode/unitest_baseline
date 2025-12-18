"""
QUESTION:
Write a function `merge_lists(list1, list2)` that merges two lists of integers into a single list. The merged list should contain elements from `list1` at even-numbered indices and elements from `list2` at odd-numbered indices. If one list is shorter than the other, append the remaining elements from the longer list in their original order. Do not use any built-in list merging functions or libraries.
"""

def entrance(list1, list2):
    merged_list = []

    len_list1 = len(list1)
    len_list2 = len(list2)
    max_length = max(len_list1, len_list2)

    for i in range(max_length):
        if i < len_list1:
            merged_list.append(list1[i])
        if i < len_list2:
            merged_list.append(list2[i])

    return merged_list