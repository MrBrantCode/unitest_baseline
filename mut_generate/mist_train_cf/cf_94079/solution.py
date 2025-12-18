"""
QUESTION:
Implement a function named `topKFrequent` that finds the k most frequently occurring elements in an array of integers. The function takes two parameters: a list of integers `nums` and a positive integer `k`. The function must return a list of the k most frequent elements in descending order of frequency. The time complexity of the function must be O(n log k), where n is the length of the array.
"""

from collections import defaultdict
import heapq

def topKFrequent(nums, k):
    # Create a hash map to store the frequency count of each element
    freq_map = defaultdict(int)
    
    # Update the frequency count in the hash map
    for num in nums:
        freq_map[num] += 1
    
    # Create a min heap to store the k most frequent elements
    min_heap = []
    
    # Iterate through the hash map
    for num, freq in freq_map.items():
        # Add the key to the heap if heap size < k
        if len(min_heap) < k:
            heapq.heappush(min_heap, (freq, num))
        else:
            # Compare the frequency count with the root element of the heap
            if freq > min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (freq, num))
    
    # Iterate through the heap to get the k most frequent elements
    result = []
    while min_heap:
        result.append(heapq.heappop(min_heap)[1])
    
    return result[::-1] # Reverse the result to get the desired order