"""
QUESTION:
Write a function `removeDuplicates(nums)` that modifies the input array `nums` in-place, allowing each number to appear no more than twice, and returns the length of the modified array. The function should use O(1) extra memory and operate within the constraints: `1 <= nums.length <= 5 * 10^4` and `-10^4 <= nums[i] <= 10^4`, where `nums` is sorted in ascending order.
"""

def removeDuplicates(nums):
    j = 1 
    count = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            count += 1
        else:
            count = 1
        if count <= 2:
            nums[j] = nums[i]
            j += 1
    return j