"""
QUESTION:
Implement a function `find_depth(nums)` that calculates the depth of a binary tree represented as a list `nums` where each node's left child is at index `2*i + 1` and right child is at index `2*i + 2`, and `None` represents the absence of a node.
"""

from collections import deque

def find_depth(nums):
    if not nums: 
        return 0
    
    nums.append(None) 
    queue = deque(nums)
    depth = 0

    while queue:
        depth += 1
        while True: 
            val = queue.popleft()
            if val is None: 
                break 
            else:
                if 2*nums.index(val)+1 < len(nums): 
                    queue.append(nums[2*nums.index(val)+1]) 
                if 2*nums.index(val)+2 < len(nums): 
                    queue.append(nums[2*nums.index(val)+2]) 
    return depth