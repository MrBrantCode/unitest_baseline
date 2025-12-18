"""
QUESTION:
Create a function `merge_sorted_lists(lst1, lst2)` that merges two sorted lists, `lst1` and `lst2`, into a new sorted list. The function should handle lists of any size and should not assume any specific values. The merged list should be returned by the function. The function should utilize the fact that the input lists are already sorted to achieve efficient performance.
"""

def merge_sorted_lists(lst1, lst2):
    merged_lst = []
    while lst1 and lst2:
        if lst1[0] < lst2[0]:
            merged_lst.append(lst1.pop(0))
        else:
            merged_lst.append(lst2.pop(0))
    merged_lst += lst1
    merged_lst += lst2
    return merged_lst