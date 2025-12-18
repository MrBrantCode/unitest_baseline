"""
QUESTION:
Implement a function named `partition` that takes a list `l` and two indices `low` and `high` as parameters. The function should rearrange the elements in the list such that all elements less than the pivot element are on its left, and all elements greater are on its right. It should return the index of the pivot element after rearrangement.

Implement a function named `quickSelect` that takes a list `l`, two indices `low` and `high`, and an integer `k` as parameters. It should use the `partition` function to find the kth smallest element in the list.

Implement a function named `median` that takes a list `l` as a parameter. It should use the `quickSelect` function to calculate the median of the list. If the list has an even number of elements, the median is the average of the two middle elements.
"""

def partition(l, low, high):
    pivot = l[high]
    i = low - 1
    for j in range(low, high):
        if l[j] <= pivot:
            i += 1
            l[i], l[j] = l[j], l[i]
    l[i+1], l[high] = l[high], l[i+1]
    return i+ 1

def quickSelect(l, low, high, k):
    if low == high:
        return l[low]

    pivotIndex = partition(l, low, high)
    if k == pivotIndex:
        return l[k]
    elif k < pivotIndex:
        return quickSelect(l, low, pivotIndex - 1, k)
    else:
        return quickSelect(l, pivotIndex + 1, high, k)    

def median(l: list):
    length = len(l)
    if length % 2 == 0:
        return (quickSelect(l, 0, length - 1, length // 2 - 1) + quickSelect(l, 0, length - 1, length // 2)) / 2
    else:
        return quickSelect(l, 0, length - 1, length // 2)