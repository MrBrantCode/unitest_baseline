"""
QUESTION:
Implement a function called `bubble_sort_recursive` that sorts a given list in descending order using a recursive bubble sort algorithm. The function should handle lists containing duplicate elements and return the sorted list.
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