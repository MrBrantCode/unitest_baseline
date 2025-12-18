"""
QUESTION:
Implement a function named "quickSort" that takes a list of integers as input and returns the sorted list in increasing order. The function should have a time complexity of O(n log n) and a space complexity of O(1), without using any built-in sorting functions, libraries, or additional data structures, and without modifying the original list. The input list will contain up to 10^5 integers in the range of -10^9 to 10^9.
"""

def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    i = -1

    for j in range(len(arr)-1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[-1] = arr[-1], arr[i+1]

    left = quickSort(arr[:i+1])
    right = quickSort(arr[i+2:])

    return left + [arr[i+1]] + right