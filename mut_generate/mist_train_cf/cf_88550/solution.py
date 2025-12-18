"""
QUESTION:
Implement the quick sort algorithm to sort a list of integers in descending order. The list may contain duplicate elements. Write a function called "quick_sort_descending" that takes in a list of integers as input and returns the sorted list.

The function should use the in-place quick sort algorithm, selecting the last element as the pivot. If there are duplicate elements equal to the pivot, they should be evenly distributed between the two sublists. The function should handle the base case when the sublist has only one element and select a new pivot element from the sublist being sorted in each recursion.

The input list will always contain at least one element and only integers.
"""

def quick_sort_descending(lst):
    def partition(lst, start, end, pivot_idx):
        pivot = lst[pivot_idx]
        lst[pivot_idx], lst[end] = lst[end], lst[pivot_idx]
        i = start
        for j in range(start, end):
            if lst[j] >= pivot:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
        lst[i], lst[end] = lst[end], lst[i]
        return i

    def quick_sort(lst, start, end):
        if start < end:
            pivot_idx = partition(lst, start, end, end)
            quick_sort(lst, start, pivot_idx - 1)
            quick_sort(lst, pivot_idx + 1, end)

    quick_sort(lst, 0, len(lst) - 1)
    return lst