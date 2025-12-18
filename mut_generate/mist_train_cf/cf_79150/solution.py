"""
QUESTION:
Implement a function `bubble_sort` that optimizes the bubble sort algorithm for sorting a list of integers, reducing unnecessary operations and improving performance. The optimized function should minimize the number of swaps and iterations when the input list is already sorted or nearly sorted.
"""

def bubble_sort(lst):
    for num in range(len(lst)-1,0,-1):
        swapped = False
        for i in range(num):
            if lst[i]>lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swapped = True
        if not swapped:
            return lst
    return lst