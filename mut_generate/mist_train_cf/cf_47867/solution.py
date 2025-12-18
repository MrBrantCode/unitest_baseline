"""
QUESTION:
Given a sequence of integers, write a function `find_smallest_product(nums)` to find the smallest product attainable from an uninterrupted subsequence. The input list `nums` may contain both positive and negative integers. The function should return the smallest product possible.
"""

def find_smallest_product(nums):
    if not nums:
        return 0
    
    global_max = local_min = local_max = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < 0:
            local_min, local_max = local_max, local_min
        local_max = max(nums[i], local_max * nums[i])
        local_min = min(nums[i], local_min * nums[i])
        
        global_max = min(global_max, local_min)
        
    return global_max