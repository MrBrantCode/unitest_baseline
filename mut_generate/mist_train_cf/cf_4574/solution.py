"""
QUESTION:
Implement a function called "quick_sort_descending" that sorts a given list of integers in descending order using the Quick Sort algorithm. The list may contain duplicate elements, and the function should modify the input list directly without creating a new list. The function should take a list of integers as input and return the sorted list. The input list will always contain at least one element and will only contain integers.
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