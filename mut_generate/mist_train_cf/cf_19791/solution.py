"""
QUESTION:
Create a function named `sort_list` that sorts a list of integers in increasing order. The function should have a time complexity of O(n^2) and not use any built-in sorting functions or methods, and it should not use any additional data structures. The input list can contain duplicate integers.
"""

def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst