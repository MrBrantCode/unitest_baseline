"""
QUESTION:
Create a function `shuffleArray` that takes an array of integers as input and returns a shuffled array where no two adjacent numbers are the same. The function should run in O(n log n) time complexity and use only constant extra space. It should also handle arrays with duplicate numbers efficiently.
"""

import heapq
from collections import Counter

def shuffleArray(nums):
    count = Counter(nums)
    max_heap = [(-freq, num) for num, freq in count.items()]
    heapq.heapify(max_heap)
    output = []
    prev_num, prev_freq = -1, 0
    
    while max_heap:
        freq, num = heapq.heappop(max_heap)
        output.append(num)
        if num == prev_num:
            if not max_heap:
                break
            next_freq, next_num = heapq.heappop(max_heap)
            output.append(next_num)
            if next_freq < -1:
                heapq.heappush(max_heap, (next_freq + 1, next_num))
        if freq < -1:
            heapq.heappush(max_heap, (freq + 1, num))
        prev_num, prev_freq = num, freq
    
    return output