"""
QUESTION:
Write a function `removeDuplicates(nums)` that takes a sorted array `nums` in ascending order and removes all duplicates in place, allowing each element to appear at most twice. Return the length of the new array.
"""

def removeDuplicates(nums):
    if len(nums) == 0:
        return 0

    count = 1
    i = 1

    while i < len(nums):
        if nums[i] == nums[i-1]:
            count += 1
        else:
            count = 1

        if count <= 2:
            i += 1
        else:
            nums.pop(i)

    return len(nums)