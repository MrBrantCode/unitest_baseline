"""
QUESTION:
Implement the `bubble_sort` function to sort a list of integers in ascending order using the bubble sort algorithm without utilizing any built-in sorting functions or methods. The function should take a list of integers as input and return the sorted list, assuming the input list will always contain at least one element.
"""

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst