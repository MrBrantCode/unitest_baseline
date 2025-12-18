"""
QUESTION:
Given an array `nums` and a value `val`, write a function `removeElement(nums, val)` that removes all instances of `val` in-place and returns the new length of the array. The function should modify the input array in-place with `O(1)` extra memory and rearrange the remaining elements in ascending order. The order of elements beyond the new length does not matter.
"""

def removeElement(nums, val):
    # Two pointers to traverse the list
    left, right = 0, len(nums) - 1

    while left <= right:
        if nums[left] == val:
            nums[left], nums[right], right = nums[right], nums[left], right - 1
        else:
            left += 1

    nums[:right+1] = sorted(nums[:right+1])

    return right + 1