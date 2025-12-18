"""
QUESTION:
Implement a function `bubble_sort_descending` that takes a list of integers as input and returns the list sorted in descending order using the Bubble Sort algorithm with a time complexity of O(n^2), where n is the length of the input list. The function should use nested loops to compare and swap adjacent elements until the list is sorted.
"""

def bubble_sort_descending(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-1):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst