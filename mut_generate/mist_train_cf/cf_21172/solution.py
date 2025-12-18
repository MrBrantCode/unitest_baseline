"""
QUESTION:
Implement a function `bubble_sort` that sorts a list of numbers in increasing order without using any built-in sorting functions or libraries, additional data structures, or modifying the original list.
"""

def bubble_sort(lst):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
    return lst