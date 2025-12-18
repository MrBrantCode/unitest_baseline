"""
QUESTION:
Implement a function named `bubble_sort` that sorts a list of positive integers in ascending order without using any built-in sorting functions or libraries. The function should take a list of integers as input and return the sorted list.
"""

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst