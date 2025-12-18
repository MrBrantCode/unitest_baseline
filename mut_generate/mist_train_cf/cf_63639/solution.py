"""
QUESTION:
Write a function named `selection_sort` that sorts a list of numbers in non-decreasing order using the selection sort algorithm. The function should also accept an optional boolean parameter `reverse` that, when set to `True`, sorts the list in non-increasing order instead. The function should return the sorted list.
"""

def selection_sort(lst, reverse=False):
    for i in range(len(lst)):
        swap = i + lst[i:].index(min(lst[i:]))
        (lst[i], lst[swap]) = (lst[swap], lst[i])

    if reverse:
        lst.reverse()
    return lst