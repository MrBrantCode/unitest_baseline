"""
QUESTION:
Create a function named `bubble_sort` that takes a list of integers as input and returns the list sorted in ascending order without using any built-in sorting functions. The function should modify the input list by repeatedly swapping adjacent elements if they are in the wrong order until the entire list is sorted.
"""

def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst