"""
QUESTION:
The function `maxSumAfterPartitioning` should take an array of integers `arr` and an integer `k` as input, and return the maximum sum that can be obtained after partitioning the array into at most `k` subarrays, where the sum of each subarray is the maximum element in the subarray multiplied by the number of elements in the subarray.
"""

import heapq

def maxSumAfterPartitioning(arr, k):
    dp = [0] * (len(arr) + 1)
    # dp[i] is going to store maximum sum we can get considering first i elements
    heap = []

    for i in range(1, len(arr)+1):
        max_e = arr[i-1]
        for j in range(1,min(i+1,k+1)):
            max_e = max(max_e, arr[i - j])
            while heap and heap[0][0] < max_e: heapq.heappop(heap)
            if i >= j:
                heapq.heappush(heap, [max_e, i - j])
            dp[i] = max(dp[i], heap[0][0] * j)

    return dp[len(arr)]