"""
QUESTION:
Implement a function named `sort_list` that takes a list of integers as input and returns the sorted list in increasing order. The function must have a time complexity of O(n^2) and cannot use any built-in sorting functions or additional data structures. The input list can contain duplicate integers and may have a length up to 10000.
"""

def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst