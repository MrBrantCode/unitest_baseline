"""
QUESTION:
Remove the duplicates from a sorted array in-place and maintain the order of the remaining elements. 

Function name: removeDuplicates(nums)

The input is a sorted array nums, and the function should modify the array in-place with O(1) extra memory. The function should return the new length of the array after duplicates are removed. The order of the remaining elements should be maintained as in the original array. 

Constraints: 0 <= nums.length <= 3 * 10^4, -10^4 <= nums[i] <= 10^4, and nums is sorted in ascending order.
"""

def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1