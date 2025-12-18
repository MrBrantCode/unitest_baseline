"""
QUESTION:
Implement a function `last_index` that takes a list of integers `nums` and a target integer `target` as input. Return the index of the last occurrence of `target` in `nums`, or -1 if `target` is not present in `nums`. The input list is not sorted.
"""

def last_index(nums, target):
    last_occurrence = -1
    for i in range(len(nums)):
        if nums[i] == target:
            last_occurrence = i
    return last_occurrence