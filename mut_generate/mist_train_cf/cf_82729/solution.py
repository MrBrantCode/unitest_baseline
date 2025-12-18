"""
QUESTION:
Write a function `find_min_k_records` that takes a list of tuples `tup_list` and an integer `k` as input. The function should return the k tuples with the smallest first elements. If the input list is empty, return "The tuple list is empty." If k is greater than the length of the list, return all elements in the list. The function should sort the tuples based on their first elements only.
"""

def find_min_k_records(tup_list, k):
    if len(tup_list) == 0:
        return "The tuple list is empty."
    if k > len(tup_list):
        return tup_list
    tup_list.sort(key=lambda x: x[0])
    return tup_list[:k]