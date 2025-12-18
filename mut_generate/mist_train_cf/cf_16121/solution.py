"""
QUESTION:
Implement the function `topKFrequent(nums, k)` that finds the k most frequently occurring elements in an array `nums`, where `k` is a given positive integer. The function should have a time complexity of O(n log k), where `n` is the length of the array `nums`. The function should return a list of the k most frequent elements in the array, in descending order of frequency.
"""

from collections import defaultdict
import heapq

def topKFrequent(nums, k):
    freq_map = defaultdict(int)
    
    for num in nums:
        freq_map[num] += 1
    
    min_heap = []
    
    for num, freq in freq_map.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (freq, num))
        else:
            if freq > min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (freq, num))
    
    result = []
    while min_heap:
        result.append(heapq.heappop(min_heap)[1])
    
    return result[::-1]