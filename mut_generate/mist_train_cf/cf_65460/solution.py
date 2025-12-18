"""
QUESTION:
You are given an array `arr` composed of integers that may or may not be distinct. The task is to divide the array into chunks or partitions, sort each chunk individually, and join them together to form a sorted array. Write a function `maxChunksToSorted` that takes the array `arr` as input and returns the maximum number of chunks that can be created.

The array `arr` has a length within the range `[1, 3000]`, and each element `arr[i]` is an integer within the range `[0, 10**9]`.
"""

def maxChunksToSorted(arr):
    sortedArr = sorted(arr) 
    chunks, prefix, sortedPrefix = 0, 0, 0
    for i in range(len(arr)):
        prefix += arr[i]
        sortedPrefix += sortedArr[i]
        if prefix == sortedPrefix:
            chunks += 1
    return chunks