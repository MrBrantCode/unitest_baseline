"""
QUESTION:
Implement a function named `bubble_sort_recursive` that sorts a list of integers in descending order using the recursive bubble sort algorithm. The input list can contain duplicate elements. The function should modify the input list in-place and return the sorted list.
"""

def bubble_sort_recursive(lst):
    swapped = False
    for i in range(len(lst) - 1):
        if lst[i] < lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            swapped = True
    if not swapped:
        return lst
    else:
        return bubble_sort_recursive(lst)