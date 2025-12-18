"""
QUESTION:
Write a function `remove_duplicates(nums)` that takes a list of integers as input, removes duplicates while preserving order, and returns the updated list. The function should have a time complexity of O(nlogn) and use no more than three variables.
"""

def remove_duplicates(nums):
    nums.sort()
    current = 0
    next = 1
    while next < len(nums):
        if nums[current] == nums[next]:
            next += 1
        else:
            current += 1
            nums[current] = nums[next]
            next += 1
    return nums[:current+1]