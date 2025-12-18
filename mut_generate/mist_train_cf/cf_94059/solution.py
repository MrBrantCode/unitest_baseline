"""
QUESTION:
Write a function `find_kth_smallest` that takes a list of integers `lst` and an integer `k` as input, and returns the kth smallest element in the list. The value of `k` is between 1 and the length of the list (inclusive), and the list may contain duplicate elements.
"""

def find_kth_smallest(lst, k):
    sorted_lst = sorted(lst)  # sort the list in ascending order
    return sorted_lst[k - 1]  # return the kth smallest element