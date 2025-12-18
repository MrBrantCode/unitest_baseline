"""
QUESTION:
Implement a function called `bubble_sort` that takes a list of integers as input, sorts it in ascending order using the bubble sort algorithm, and returns the sorted list. The input list will always contain at least one element.
"""

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        # Last i elements are already in place
        for j in range(n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst