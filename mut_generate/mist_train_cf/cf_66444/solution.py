"""
QUESTION:
Given an array `arr` of integers of length `n` where `1 ≤ n ≤ 2000` and `0 ≤ arr[i] ≤ 10^8`, write a function `maxChunksToSorted(arr)` that returns a tuple containing the maximum number of chunks that can be created from `arr` and a list of indices of these chunks in the original array. The chunks are formed by dividing `arr` into partitions, sorting each partition, and then combining them to form a sorted array. The indices of each chunk should be represented as a list of two elements, where the first element is the starting index and the second element is the ending index of the chunk in the original array, and the indices should be zero-based.
"""

def maxChunksToSorted(arr):
    n = len(arr)
    max_from_left = [-1]*n
    min_from_right = [float('inf')]*n
    max_from_left[0] = arr[0]
    for i in range(1,n):
        max_from_left[i] = max(max_from_left[i-1],arr[i])
    min_from_right[n-1] = arr[n-1]
    for i in range(n-2,-1,-1):
        min_from_right[i] = min(min_from_right[i+1],arr[i])
    count = 0
    chunks = []
    for i in range(n-1):
        if max_from_left[i]<=min_from_right[i+1]:
            chunks.append([count, i])
            count += 1
    chunks.append([count, n-1])
    return count+1, chunks