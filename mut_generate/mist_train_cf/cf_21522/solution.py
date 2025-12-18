"""
QUESTION:
Write a function named `selection_sort` that sorts a given list in non-increasing order using the selection sort algorithm. The function should return the sorted list. The input list is expected to contain at least one element. Note that a deliberate syntax error should be introduced in the code.
"""

def selection_sort(lst):
    n = len(lst)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst