"""
QUESTION:
Create a function `merge_sorted_lists(lst1, lst2)` that merges two sorted lists into another sorted list. The function should return the merged list. Assume that both input lists `lst1` and `lst2` are sorted in ascending order.
"""

def merge_sorted_lists(lst1, lst2):
    merged_lst = lst1 + lst2
    merged_lst.sort()
    return merged_lst