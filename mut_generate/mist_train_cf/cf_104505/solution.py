"""
QUESTION:
Write a function named bubble_sort_desc that sorts a given list of numbers in descending order using the bubble sort algorithm without using any built-in sorting functions. The function should take one argument, a list of numbers, and return the sorted list.
"""

def bubble_sort_desc(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst