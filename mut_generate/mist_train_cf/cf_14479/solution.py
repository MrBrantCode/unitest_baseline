"""
QUESTION:
Implement a function `bubble_sort(arr)` that takes an array of integers as input and returns the array sorted in ascending order using the bubble sort algorithm. The function should modify the input array in-place and terminate when no more swaps are needed. The input array may contain duplicate elements.
"""

def entance(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    return arr