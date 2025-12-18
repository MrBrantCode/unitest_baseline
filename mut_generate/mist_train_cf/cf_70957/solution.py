"""
QUESTION:
Implement the function `convertMinHeap(arr)` that takes an array `arr` as input and returns the minimum number of swaps required to convert the array into a min-heap. The function should utilize two helper functions: `isMinHeap(arr, i, n)` to check if a subtree is a min-heap, and `heapify(arr, i, num_swaps)` to heapify a subtree. The `heapify` function should return the updated number of swaps.
"""

def isMinHeap(arr, i, n):
    if 2 * i + 1 < n:
        if arr[i] > arr[2 * i + 1]:
            return False
    if 2 * i + 2 < n:
        if arr[i] > arr[2 * i + 2]:
            return False
    return True


def heapify(arr, i, num_swaps):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < len(arr) and arr[i] > arr[left]:
        smallest = left

    if right < len(arr) and arr[smallest] < arr[right]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        num_swaps += 1
        num_swaps = heapify(arr, smallest, num_swaps)

    return num_swaps


def convertMinHeap(arr):
    if not isMinHeap(arr, 0, len(arr)):
        num_swaps = 0
        for i in range((len(arr)-1)//2, -1, -1):
            num_swaps = heapify(arr, i, num_swaps)
        return num_swaps
    else:
        return 0