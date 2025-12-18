"""
QUESTION:
Given a sorted array `nums`, modify it in-place such that duplicates appear at most twice and return the new length. The function should also keep track of the number of unique elements in the array. The modification should be done with O(1) extra memory, and the input array should be modified in-place. The function should return the count of unique elements and the new length of the array.

Constraints: `1 <= nums.length <= 3 * 10^4`, `-10^4 <= nums[i] <= 10^4`, and `nums` is sorted in ascending order.
"""

def entance(nums):
    if len(nums) < 3: return len(set(nums)), len(nums)
    pos = 2
    unique = 1
    for i in range(2, len(nums)):
        if nums[i] != nums[pos - 2]:
            nums[pos] = nums[i]
            pos += 1
        if nums[i] != nums[i - 1]:
            unique += 1
    return unique, pos