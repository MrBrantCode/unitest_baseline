"""
QUESTION:
Implement a function named `mergeSort` that takes a list of integers as input, sorts the list in ascending order using the Merge Sort algorithm, and returns the sorted list. The function should not use any built-in sorting functions or data structures, should have a time complexity of O(n log n), and should maintain the relative order of elements with equal values.
"""

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    leftPointer = 0
    rightPointer = 0

    while leftPointer < len(left) and rightPointer < len(right):
        if left[leftPointer] <= right[rightPointer]:
            merged.append(left[leftPointer])
            leftPointer += 1
        else:
            merged.append(right[rightPointer])
            rightPointer += 1

    while leftPointer < len(left):
        merged.append(left[leftPointer])
        leftPointer += 1

    while rightPointer < len(right):
        merged.append(right[rightPointer])
        rightPointer += 1

    return merged