"""
QUESTION:
Write a function named `insertion_sort` that sorts a list of positive integers in ascending order. The function must preserve the original order of duplicate integers. The list can contain up to 100,000 elements. The function should return the sorted list.
"""

def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst