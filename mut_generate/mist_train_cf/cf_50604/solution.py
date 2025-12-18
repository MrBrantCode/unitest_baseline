"""
QUESTION:
Create a function named `bubble_sort` that sorts a given list of integers in ascending order without using any built-in sorting library functions. The function should take one argument, a list of integers, and return the sorted list.
"""

def bubble_sort(list_1):
    for i in range(len(list_1) - 1):
        for j in range(len(list_1) - 1 - i):
            if list_1[j] > list_1[j + 1]:
                list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j]     # Swap elements
    return list_1