"""
QUESTION:
Function Name: minimumSize
Description: You are given an integer array `nums` where the `ith` basket contains `nums[i]` apples and an integer `maxOperations`. Perform the operation of dividing any basket into two new baskets with a positive number of apples at most `maxOperations` times. Return the maximum possible penalty (minimum number of apples in a basket) after the operations.
Restrictions: 1 <= nums.length <= 10^5, 1 <= maxOperations, nums[i] <= 10^9
"""

import heapq

def minimumSize(nums, maxOperations):
    heap = [-num for num in nums]  
    heapq.heapify(heap)
    while maxOperations > 0:
        max_val = -heapq.heappop(heap)
        quotient, remainder = divmod(max_val, 2)
        heapq.heappush(heap, -quotient)
        if remainder > 0:
            heapq.heappush(heap, -remainder)
        maxOperations -= 1
    return -heap[0]