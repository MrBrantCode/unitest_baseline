"""
QUESTION:
Implement a function named `find_kth_largest` that takes an array of integers `nums` and an integer `k` as input. The function should return the kth largest element in the array without using any built-in sorting or priority queue functions. The time complexity of the function should be O(n log k), and the space complexity should be O(k).
"""

import heapq

def findKthLargest(nums, k):
    min_heap = []

    # Add the first k elements to the min heap
    for i in range(k):
        heapq.heappush(min_heap, nums[i])

    # Compare remaining elements with the root of the min heap
    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, nums[i])

    # Return the root of the min heap
    return min_heap[0]