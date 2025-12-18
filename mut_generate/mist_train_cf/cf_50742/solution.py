"""
QUESTION:
Implement a function called `median` that calculates the median element of an unsorted list of numbers using the QuickSelect algorithm. The `median` function should call a helper function called `quick_select` which takes a list and an index, and returns the element at that index if the list were sorted. The `quick_select` function should use another helper function called `partition` to partition the list around a pivot element. The `partition` function should rearrange the list such that all elements less than the pivot are to its left, and all elements greater are to its right, and return the index of the pivot.
"""

def partition(lst, low, high):
    """Rearrange the list such that all elements less than the pivot are to its left,
    and all elements greater are to its right, and return the index of the pivot.
    """
    pivot = lst[high]
    i = low - 1
    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1

def quick_select(lst, k):
    """Return the element at index k if the list were sorted.
    """
    if len(lst) == 1:
        return lst[0]
    pivot_index = partition(lst, 0, len(lst) - 1)
    if pivot_index == k:
        return lst[pivot_index]
    elif pivot_index > k:
        return quick_select(lst[:pivot_index], k)
    else:
        return quick_select(lst[pivot_index + 1:], k - pivot_index - 1)

def median(lst):
    """Calculate the median element of an unsorted list of numbers using the QuickSelect algorithm.
    """
    n = len(lst)
    mid1 = quick_select(lst, n // 2)
    mid2 = None
    if n % 2 == 0:
        mid2 = quick_select(lst, n // 2 - 1)
        return (mid1 + mid2) / 2
    else:
        return mid1