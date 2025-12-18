"""
QUESTION:
Write a function named `removeDuplicates` that takes a sorted array in ascending order and removes all duplicates that occur more than twice in place. The function should return the length of the new array after removal.
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