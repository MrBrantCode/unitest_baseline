"""
QUESTION:
Write a function `find_highest_numbers` that takes an array of integers `nums` as input and returns the 3 highest distinct numbers in descending order. The function should have a time complexity of O(n log n) or better and use constant space. The input array will contain at most 10^5 integers, ranging from -10^9 to 10^9.
"""

import heapq

def find_highest_numbers(nums):
    distinct_nums = set()
    heap = []
    
    for num in nums:
        if num not in distinct_nums:
            distinct_nums.add(num)
            heapq.heappush(heap, num)
            if len(heap) > 3:
                heapq.heappop(heap)
    
    highest_numbers = []
    while heap:
        highest_numbers.append(heapq.heappop(heap))
    
    return highest_numbers[::-1]