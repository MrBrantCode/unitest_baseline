"""
QUESTION:
Implement a function `topKFrequent(nums, k)` that finds the k most frequently occurring elements in an array `nums`, where k is a given positive integer. The function should return an array of the k most frequent elements in non-increasing order of frequency. If there are multiple elements with the same frequency, the smaller elements should be placed first. The time complexity of the function should be O(n log k), where n is the length of the array. The input array should not be modified.
"""

import heapq

def topKFrequent(nums, k):
    # Create a hash map to store the frequency of each element
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    # Create a min heap to store the k most frequent elements
    min_heap = []
    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Create the result array
    result = []
    while min_heap:
        result.append(heapq.heappop(min_heap)[1])

    # Reverse the result array to maintain non-increasing order of frequency
    result.reverse()

    return result