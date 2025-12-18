"""
QUESTION:
Write a function called bubble_sort that takes a list of integers as input and returns the sorted list in ascending order using the bubble sort algorithm. The input list will always contain at least one element.
"""

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst