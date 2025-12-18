"""
QUESTION:
Given an array of integers `arr`, split the array into the maximum number of "chunks" (partitions), individually sort each chunk, and concatenate them to form a sorted array. The function should return the maximum number of chunks possible.

The function name is `maxChunksToSorted` and it takes an array of integers `arr` as input. The length of `arr` is in the range `[1, 10]` and each element `arr[i]` is an integer in the range `[1, 100]`.
"""

def maxChunksToSorted(arr):
    max_of_left = [None] * len(arr)
    max_of_left[0] = arr[0]
    for i in range(1, len(arr)):
        max_of_left[i] = max(max_of_left[i-1], arr[i])

    min_of_right = [None] * len(arr)
    min_of_right[-1] = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        min_of_right[i] = min(min_of_right[i+1], arr[i])
      
    chunks = 0
    for i in range(0, len(arr)-1):
        if max_of_left[i] <= min_of_right[i+1]:
            chunks += 1

    return chunks+1