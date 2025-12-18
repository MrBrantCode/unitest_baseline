"""
QUESTION:
Write a function `mergeAndSort(nums, n)` that takes two parameters: `nums` as a list of sorted integer arrays and `n` as a list of integers representing the number of elements in each array in `nums`. The function should merge the arrays in `nums` into one sorted array. Assume that `nums[i].length == n[i]`, `0 <= n[i] <= 200`, `1 <= sum(n[i]) <= 200`, `-109 <= nums[i][j] <= 109`, and `1 <= k <= 10` where `k` is the number of arrays in `nums`.
"""

import heapq 

def mergeAndSort(nums, n):
    result = []
    heap = []
    
    for i in range(len(nums)):
        if n[i] > 0:
            heapq.heappush(heap, (nums[i][0], i, 1)) 
    
    while heap:
        current_smallest, array_index, element_index = heapq.heappop(heap)
        result.append(current_smallest)
        
        if element_index < n[array_index]:
            heapq.heappush(
                heap, (nums[array_index][element_index], array_index, element_index + 1))
    
    return result