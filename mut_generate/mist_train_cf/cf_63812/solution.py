"""
QUESTION:
Design a function named `findKthSmallest` that takes an unsorted list of integers `nums` and an integer `k` as input, and returns the kth smallest integer in `nums`. The function should adhere to a time complexity of O(n log k). If `k` is greater than the length of `nums`, the function should return `None`.
"""

import heapq

def findKthSmallest(nums, k):
    if k > len(nums):
        return None   

    # Initialize max heap
    heap = []
    for num in nums:
        heapq.heappush(heap, -num)
        
        # If heap size > k, pop out the max element
        if len(heap) > k:
          heapq.heappop(heap)

    # The root of heap is the Kth smallest number
    return -heap[0]