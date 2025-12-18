"""
QUESTION:
Implement a function named `stable_sort` that takes a list of integers as input and returns the list sorted in ascending order. The function must preserve the relative order of numbers that are the same and cannot use any built-in or library sort functions. The function should implement a stable sorting algorithm.
"""

def stable_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >=0 and key < lst[j] :
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst