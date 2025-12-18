"""
QUESTION:
Implement a function `median(l)` that estimates the median of a list `l` without sorting the list or using library functions. The list `l` can contain negative integers, zero, or be empty. The function should return the median if the list is not empty, or 'Error' if the list is empty.
"""

def partition(lst, low, high):
    pivotIndex = low
    pivot = lst[pivotIndex]
    while low < high:
        while low < len(lst) and lst[low] <= pivot:
            low += 1
        while lst[high] > pivot:
            high -= 1
        if(low < high):
            lst[low], lst[high] = lst[high], lst[low]
    lst[high], lst[pivotIndex] = lst[pivotIndex], lst[high]
    return high

def quick_select(lst, k):
    if len(lst) == 1 or k < 0 or k >= len(lst):
        return lst[0]
    pivotIndex = partition(lst, 0, len(lst) - 1)
    if pivotIndex == k:
        return lst[pivotIndex]
    elif pivotIndex > k:
        return quick_select(lst[0:pivotIndex], k)
    else:
        return quick_select(lst[pivotIndex + 1:], k - pivotIndex - 1)

def median(l):
    if len(l) == 0:
        return "Error"
    elif len(l) % 2 == 1:
        return quick_select(l, len(l) // 2)
    else:
        return 0.5 * (quick_select(l, len(l) // 2 - 1) + quick_select(l, len(l) // 2))