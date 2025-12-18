"""
QUESTION:
Write a function `quick_Sort` that takes in the following parameters:
- `lst`: a list of integers to be sorted.
- `first`: an integer representing the leftmost index of the subsequence to be sorted.
- `last`: an integer representing the rightmost index of the subsequence to be sorted.

Your function should sort the subsequence of the input list `lst` within the range defined by the `first` and `last` indices in ascending order using the in-place quicksort algorithm.
"""

def partition(lst, first, last):
    pivot = lst[last]
    i = first - 1
    for j in range(first, last):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[last] = lst[last], lst[i + 1]
    return i + 1

def quick_Sort(lst, first, last):
    if first < last:
        pivot_index = partition(lst, first, last)
        quick_Sort(lst, first, pivot_index - 1)
        quick_Sort(lst, pivot_index + 1, last)