"""
QUESTION:
Write a function `findShortestSubarray` that takes an array of integers `nums` and an integer `k` as input, and returns the length of the shortest subarray that sums up to `k`. If no such subarray exists, return -1. The function should iterate through the array only once, with a time complexity of O(n), where n is the length of the input array.
"""

def findShortestSubarray(nums, k):
    shortest_length = float('inf')
    prefix_sum = 0
    sum_indices = {0: -1}
    
    for i in range(len(nums)):
        prefix_sum += nums[i]
        
        if prefix_sum - k in sum_indices:
            shortest_length = min(shortest_length, i - sum_indices[prefix_sum - k])
        
        if prefix_sum not in sum_indices:
            sum_indices[prefix_sum] = i
    
    return -1 if shortest_length == float('inf') else shortest_length