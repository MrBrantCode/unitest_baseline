"""
QUESTION:
Write a function named `find_pair` that takes a list of integers `nums` and a target integer `target` as input. The function should return a list containing two distinct integers from `nums` that add up to `target` in ascending order. If there are multiple pairs, return the pair with the smallest absolute difference between the two integers. If no such pair exists, return an empty list.
"""

def find_pair(nums, target):
    if len(nums) < 2:
        return []
    
    num_set = set()
    for num in nums:
        if target - num in num_set:
            return sorted([num, target - num])
        num_set.add(num)
    
    return []