"""
QUESTION:
Given an array `arr` of integers with a length between 1 and 2000 and values between 0 and 10^8, write a function `maxChunksToSorted` to divide the array into the maximum number of "chunks" or partitions such that when each chunk is sorted individually and joined together, the outcome is a sorted array.
"""

def maxChunksToSorted(arr):
    n = len(arr)
    left_max = [0]*n
    right_min = [float('inf')]*(n+1)

    left_max[0] = arr[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], arr[i])
    
    right_min[-2] = arr[-1]
    for i in range(n-2, -1, -1):
        right_min[i] = min(right_min[i+1], arr[i])
    
    chunks = sum([left_max[i] <= right_min[i+1] for i in range(n-1)])
    
    return chunks + 1