"""
QUESTION:
Write a function `can_jump` that takes a list of non-negative integers `nums` representing the maximum jump length from each position and returns `True` if the last index can be reached, and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the input list, and only iterate through the list once.
"""

def canJump(nums):
    max_reachable = 0
    for i in range(len(nums)):
        if i > max_reachable:
            return False
        max_reachable = max(max_reachable, i + nums[i])
        if max_reachable >= len(nums) - 1:
            return True
    return False