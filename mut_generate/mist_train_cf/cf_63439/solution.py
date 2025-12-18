"""
QUESTION:
Function: check(nums)

The function should determine if the given array `nums` was initially sorted in a non-decreasing sequence and then subjected to a rotation of a certain number of positions. The function should return `true` if the array is sorted and rotated, and `false` otherwise.

Restrictions: 
1. `1 <= nums.length <= 100`
2. `1 <= nums[i] <= 100`
"""

def check(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] > nums[(i+1)%len(nums)]: 
            count += 1
    return count <= 1