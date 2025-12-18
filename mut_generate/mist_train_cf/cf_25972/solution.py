"""
QUESTION:
Implement an iterative mergesort algorithm with a time complexity of O(nlog(n)), that takes a list of elements as input, splits it into its two halves, sorts each half, and then merges the sorted halves.
"""

def entrance(arr):
    width = 1
    while width < len(arr):
        for i in range(0, len(arr), 2 * width):
            merge(arr, i, min(i + width, len(arr)), min(i + 2 * width, len(arr)))
        width *= 2
    return arr

def merge(arr, low, mid, high):
    left = arr[low:mid]
    right = arr[mid:high]
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    arr[low:high] = result