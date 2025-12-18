"""
QUESTION:
Find the k most frequently occurring elements in an array, where k is a given positive integer. The array may contain duplicate elements. Implement an algorithm with a time complexity of O(n log k), where n is the length of the array.

Input: 
- An array of integers.
- A positive integer k.

Output: 
An array of the k most frequently occurring elements in the input array, sorted in non-increasing order of the frequency of occurrence. If there are multiple elements with the same frequency of occurrence, the smaller elements should be placed first.

Restrictions:
- The input array will always have at least k distinct elements.
- The overall time complexity should be O(n log k).
- Additional data structures can be used.
- The input array should not be modified.
"""

import heapq

def topKFrequent(nums, k):
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    min_heap = []
    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    result = []
    while min_heap:
        result.append(heapq.heappop(min_heap)[1])

    result.reverse()
    return result