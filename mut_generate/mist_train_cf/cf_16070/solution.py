"""
QUESTION:
Write a function named `find_kth_smallest` that takes a list of integers and an integer `k` as input, and returns the kth smallest element from the list. The list may contain duplicate elements, and k is an integer greater than or equal to 1 and less than or equal to the length of the list.
"""

def find_kth_smallest(lst, k):
    sorted_lst = sorted(lst)  # sort the list in ascending order
    return sorted_lst[k - 1]  # return the kth smallest element