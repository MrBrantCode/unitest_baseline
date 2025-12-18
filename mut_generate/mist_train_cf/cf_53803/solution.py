"""
QUESTION:
Write a function `minHeapify(arr, n, i, swaps)` that takes an array `arr`, its length `n`, an index `i`, and the number of swaps `swaps` as input. This function should ensure the min heap property at index `i` in the array. If the element at index `i` is not the smallest among its children, the function should swap it with the smallest child and recursively call itself on the affected sub-tree. The function should return the updated number of swaps.

Additionally, write the following functions:

- `buildMinHeap(arr)`: takes an array as input, calls `minHeapify` on each non-leaf node in reverse level order, and returns the array and the total number of swaps made.
- `isMinHeap(arr)`: checks if the given array satisfies the min heap property and returns a boolean value.
- `createMinHeap(arr)`: checks if the given array is already a min heap. If it is, return the array and 0 swaps. If not, call `buildMinHeap` on the array and return the result.
"""

def minHeapify(arr, n, i, swaps):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] > arr[left]:
        smallest = left

    if right < n and arr[smallest] > arr[right]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        swaps += 1
        swaps = minHeapify(arr, n, smallest, swaps)

    return swaps


def buildMinHeap(arr):
    swaps = 0
    for i in range(len(arr) // 2 - 1, -1, -1):
        swaps = minHeapify(arr, len(arr), i, swaps)
    return arr, swaps


def isMinHeap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        if 2 * i + 1 < n and arr[i] > arr[2 * i + 1]:
            return False
        if 2 * i + 2 < n and arr[i] > arr[2 * i + 2]:
            return False   
    return True


def createMinHeap(arr):
    if isMinHeap(arr):
        return arr, 0
    else:
        return buildMinHeap(arr)