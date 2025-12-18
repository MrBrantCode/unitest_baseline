"""
QUESTION:
Create a function `merge_sorted_lists(l1, l2)` that takes two sorted lists `l1` and `l2` as input and returns a single sorted list containing all elements from both lists. The function should run in O(N) time, where N is the total number of elements in the two lists. The function can use O(N) additional space to store the merged list. The input lists `l1` and `l2` should not be modified.
"""

def merge_sorted_lists(l1, l2):
    merged_list = []
    i = 0
    j = 0

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            merged_list.append(l1[i])
            i += 1
        else:
            merged_list.append(l2[j])
            j += 1

    while i < len(l1):
        merged_list.append(l1[i])
        i += 1

    while j < len(l2):
        merged_list.append(l2[j])
        j += 1

    return merged_list