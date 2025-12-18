"""
QUESTION:
Given a list of integers `nums` and an integer `target`, write a function `maxSubarrayLen(nums, target)` that returns the maximum length of a contiguous subarray that sums to `target`. If no such subarray exists, return 0. The input list `nums` and the integer `target` are the only inputs to the function, and the function should return an integer representing the maximum length of the contiguous subarray.
"""

def maxSubarrayLen(nums, target):
    s = 0  
    last = {}  
    
    for i in range(len(nums)):
        s += nums[i]  
        
        if s - target in last:  
            max_len = max((last[s - target] + 1), (last.get(s - target - nums[i], 0) + 1))
            last[s] = max(last.get(s, 0), max_len + (i - max_len))
        else:  
            if s == target:
                last[s] = i
            else:
                last[s] = -1
    return last.get(target, 0)