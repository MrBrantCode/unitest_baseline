"""
QUESTION:
Given an array `arr` of integers (not necessarily distinct) with a length in range `[1, 3000]` and elements in range `[0, 10**9]`, write a function `maxChunksToSorted` that splits the array into the maximum number of "chunks" (partitions), individually sorts each chunk, and returns the maximum number of chunks that can be made such that the concatenated result equals the sorted array.
"""

def maxChunksToSorted(arr):
    # store cumulative sum of original and sorted array
    sum1, sum2 = 0, 0
    chunks = 0

    # sort the array 
    sorted_arr = sorted(arr)
    for a, b in zip(arr, sorted_arr):
        # accumulate original and sorted array
        sum1 += a
        sum2 += b

        # if cumulative sum is same increment chunks.
        if sum1 == sum2:
            chunks += 1

    return chunks