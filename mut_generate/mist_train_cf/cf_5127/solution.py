"""
QUESTION:
Write a function `heapsort_with_min_heap` that sorts an array of integers using a modified version of the heapsort algorithm with a min-heap data structure. The input array may contain duplicates and negative integers, and the time complexity of the algorithm should be O(n log k), where n is the length of the input array and k is the number of distinct elements in the input array.
"""

import heapq
from collections import defaultdict

def heapsort_with_min_heap(arr):
    distinct_elements = defaultdict(int)
    for num in arr:
        distinct_elements[num] += 1

    min_heap = []
    for num, freq in distinct_elements.items():
        heapq.heappush(min_heap, (num, freq))

    result = []
    while min_heap:
        num, freq = heapq.heappop(min_heap)
        result.extend([num] * freq)
        if num in distinct_elements:
            distinct_elements[num] -= freq
            if distinct_elements[num] == 0:
                del distinct_elements[num]
            else:
                heapq.heappush(min_heap, (num, distinct_elements[num]))

    return result