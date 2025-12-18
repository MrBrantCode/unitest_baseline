"""
QUESTION:
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements in any order. If multiple elements have the same frequency, return the element with the smaller value. The time complexity of the solution must be better than `O(n log n)`, where `n` is the array's size. 

Function name: `topKFrequent(nums, k)`
"""

import heapq
from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums) 
    heap = []

    for num, freq in count.items():
        # Python's heapq is a min-heap, so we invert freq to sort in decreasing order
        if len(heap) < k: 
            heapq.heappush(heap, (freq, num))
        else:
            # Only push to the heap if the current frequency is greater than the min frequency in the heap
            if freq > heap[0][0]:
                heapq.heapreplace(heap, (freq, num))

    return [x[1] for x in heap]