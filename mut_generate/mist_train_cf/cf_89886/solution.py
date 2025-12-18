"""
QUESTION:
Implement a function `find_kth_largest(arr, k)` that finds the k-th largest element in a list of integers. The function should return the k-th largest element if it exists, otherwise return `None`. The time complexity of the function should be O(nlogk), where n is the length of the list.
"""

import heapq

def find_kth_largest(arr, k):
    if len(arr) < k:
        return None
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0] if len(heap) == k else None