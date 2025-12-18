"""
QUESTION:
Create a function called find_kth_largest that takes in a list of integers (arr) and an integer (k) as input parameters. The function should return the k-th largest element in the list. If there is no k-th largest element (i.e., k is larger than the length of the list), the function should return None. The function should handle lists with duplicate values, negative integers, empty lists, and lists with only one element correctly. The time complexity of the function should be O(nlogk), where n is the length of the list.
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