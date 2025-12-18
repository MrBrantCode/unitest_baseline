"""
QUESTION:
Write a function `removeDuplicates(nums)` that takes an array of integers and removes all duplicates in place, returning the length of the new array. The function should also remove any duplicates that occur more than twice. The input array may be unsorted. The implementation should have a time complexity of O(n) and should not use any additional data structures.
"""

def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)

    prev = nums[0]
    count = 1
    result = 1

    for i in range(1, len(nums)):
        if nums[i] == prev:
            count += 1
            if count <= 2:
                nums[result] = nums[i]
                result += 1
        else:
            prev = nums[i]
            nums[result] = nums[i]
            result += 1
            count = 1

    return result