"""
QUESTION:
Implement a function named `selection_sort` that takes a list of integers as a parameter and returns the sorted list in ascending order using the selection sort algorithm. The list can be of any length and contain any integer values. The function should modify the original list and return the sorted list.
"""

def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst