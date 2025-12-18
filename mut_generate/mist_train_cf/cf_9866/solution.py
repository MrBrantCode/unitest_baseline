"""
QUESTION:
Create a function called `search_list` that takes a list of integers `nums` and a target integer `target` as parameters. The function should return the index of the first occurrence of `target` in `nums` if found, and -1 if `target` does not exist in `nums`. The function should handle the case where the input list is empty.
"""

def search_list(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1