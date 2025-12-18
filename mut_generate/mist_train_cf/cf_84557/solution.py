"""
QUESTION:
Write a function named `find_kth_smallest` that takes an array `arr` of distinct elements and an integer `k` as input, and returns the Kth smallest element in the array. The function should return `None` if `k` is less than or equal to 0 or greater than the length of the array. Assume all elements in the array are distinct.
"""

import heapq

def find_kth_smallest(arr, k):
    if k <= len(arr) and k > 0:
        # Make all elements in arr negative and put it in max-heap
        max_heap = [-num for num in arr]
        heapq.heapify(max_heap)

        # Remove the root(max element) k times
        for _ in range(k):
            smallest = heapq.heappop(max_heap)

        # The root of the max heap now is the kth smallest element in arr
        return -smallest

    return None