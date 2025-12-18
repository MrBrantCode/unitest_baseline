"""
QUESTION:
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:


Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

Note:

You can assume that you can always reach the last index.
"""

def minimum_jumps_to_end(nums):
    if len(nums) == 1:
        return 0
    
    step = 0
    pos = 0
    
    while pos != len(nums) - 1:
        best_step = -1
        best_value = -1
        
        for i in range(nums[pos], 0, -1):
            if len(nums) - 1 == pos + i:
                best_step = i
                break
            if pos + i < len(nums) and nums[pos + i] != 0 and (nums[pos + i] + i > best_value):
                best_step = i
                best_value = nums[pos + i] + i
        
        pos += best_step
        step += 1
    
    return step