"""
QUESTION:
Create a function `kthMaximum(nums, k)` that returns the kth maximum element in an array `nums` with length `n`, where the numbers in the array might not be distinct, and the function should work within a time complexity of O(n*log(k)). Create another function `sumKthMaxElements(nums, k)` that finds the sum of kth maximum elements from 1 to k using an efficient data structure.
"""

import heapq

def kthMaximum(nums, k):
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
    return heap[0]

def sumKthMaxElements(nums, k):
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
    return sum(heap)