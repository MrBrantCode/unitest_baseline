"""
QUESTION:
Write a function `removeDuplicates(nums)` that takes an array `nums` as input and removes all duplicates that occur more than twice in place, returning the length of the new array.
"""

def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)

    index = 2  # Start from the third element since the first two elements are always unique
    for i in range(2, len(nums)):
        if nums[i] != nums[index - 2]:
            nums[index] = nums[i]
            index += 1

    return index