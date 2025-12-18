"""
QUESTION:
Implement a function `mergeSort()` that takes an array of integers as input and returns a new array with the elements sorted in inverse numerical order. The function should have a time complexity of O(n log n) and should handle duplicate elements without changing their original order. Do not use any built-in sorting functions or data structures.
"""

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    mergedArray = []
    leftPointer = 0
    rightPointer = 0

    while leftPointer < len(left) and rightPointer < len(right):
        if left[leftPointer] > right[rightPointer]:
            mergedArray.append(left[leftPointer])
            leftPointer += 1
        else:
            mergedArray.append(right[rightPointer])
            rightPointer += 1

    while leftPointer < len(left):
        mergedArray.append(left[leftPointer])
        leftPointer += 1

    while rightPointer < len(right):
        mergedArray.append(right[rightPointer])
        rightPointer += 1

    return mergedArray