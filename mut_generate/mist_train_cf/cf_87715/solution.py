"""
QUESTION:
Implement a function called `findMedian` that takes an array of integers as input and returns the median of the array. The function must sort the array in-place using the Quick Sort algorithm without using any extra space or built-in sorting functions. The partitioning step of the Quick Sort algorithm should be implemented in a recursive manner without using explicit recursion.
"""

def findMedian(arr):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

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

    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2] + arr[n//2 - 1]) / 2
    else:
        return arr[n//2]