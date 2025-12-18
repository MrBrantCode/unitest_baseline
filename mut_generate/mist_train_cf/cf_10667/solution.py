"""
QUESTION:
Write a function named `find_kth_largest` that takes an array of integers `nums` and an integer `k` as input. Implement the function without using any built-in sorting or priority queue functions. The function should return the kth largest element in the array. The time complexity of your algorithm should be O(n log k), and the space complexity should be O(k).
"""

import heapq

def find_kth_largest(nums, k):
    min_heap = []

    for i in range(k):
        heapq.heappush(min_heap, nums[i])

    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, nums[i])

    return min_heap[0]