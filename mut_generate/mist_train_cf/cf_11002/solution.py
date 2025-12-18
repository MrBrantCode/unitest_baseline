"""
QUESTION:
Implement a function named 'bubble_sort' that takes a list of integers as input and returns the list sorted in descending order, without using any built-in sorting functions or libraries.
"""

def bubble_sort(lst):
    n = len(lst)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst