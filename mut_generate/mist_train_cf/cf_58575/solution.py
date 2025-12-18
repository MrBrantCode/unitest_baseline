"""
QUESTION:
Implement the Quick Sort algorithm to sort a given array of n elements within a time complexity limit of O(nlogn). Implement the function `qsort(arr)` where `arr` is the input array of integers. The function should return the sorted array. The input array can contain duplicate elements.
"""

def qsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return qsort(left) + middle + qsort(right)