"""
QUESTION:
Implement a function called `findMedian` that takes an array of integers as input and returns the median of the array. The function should first sort the array in-place using the Quick Sort algorithm with an iterative approach (no explicit recursion or extra space). The Quick Sort algorithm should use a stack to simulate the recursion and a partition function to rearrange the elements. After sorting, the function should find the middle element of the sorted array. The array can have an even or odd number of elements, and the function should handle both cases correctly.
"""

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quickSort(arr):
    stack = []
    stack.append((0, len(arr) - 1))
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = partition(arr, low, high)
            if pivot - 1 > low:
                stack.append((low, pivot - 1))
            if pivot + 1 < high:
                stack.append((pivot + 1, high))

def findMedian(arr):
    quickSort(arr)
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2] + arr[n//2 - 1]) / 2
    else:
        return arr[n//2]