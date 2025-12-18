"""
QUESTION:
Implement a function called `mergeSort` that sorts a given array of integers in ascending order. The function should not use any built-in sorting functions or libraries and have a time complexity of O(n log n) and a space complexity of O(n). The function should handle duplicate integers and return the sorted array as a new array, leaving the original array unchanged.
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
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            mergedArray.append(left[i])
            i += 1
        else:
            mergedArray.append(right[j])
            j += 1

    mergedArray.extend(left[i:])
    mergedArray.extend(right[j:])

    return mergedArray